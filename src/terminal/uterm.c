/**************************************************
TODO's:
 * Come up with a better name
 * Actually set up serial port stuff
 * Add config file
 * Add command line arguments
 * Add ability to log to file
 * add ability to send/upload files
 * better document code / general code cleanup
 * ability to execute terminal commands (ex: !ls, !cd, etc)
 * check different baud rates / parity issues
 * autoselect serial port

 **************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <readline/readline.h>
#include <readline/history.h>

#include <sys/select.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define RED   "\x1B[31m"
#define GRN   "\x1B[32m"
#define YEL   "\x1B[33m"
#define BLU   "\x1B[34m"
#define MAG   "\x1B[35m"
#define CYN   "\x1B[36m"
#define WHT   "\x1B[37m"
#define RST   "\x1B[0m"


#define MAX_BUF 256


const char * prompt = CYN "PROMPT> " RST;


int serialFD;

/* 
   Uses nonblocking Readline sample code from:
       stackoverflow.com/questions/1512028/

   And general code for reading/writing to a serial device.
    (it turns out you just ... read and write to it. wow.)

 */
void printSerial(int serialFD) {
   /* function called when serial input recieved. It clears the
      current user input, prints input from serial, and then 
      redisplays what the user was typing*/
   static char buf[MAX_BUF];
   char* saved_line;
   int saved_point, size;
   saved_point = rl_point;
   saved_line = rl_copy_text(0, rl_end);
   rl_set_prompt("");
   rl_replace_line("", 0);
   rl_redisplay();


   usleep(20000);   		/* sleep 20ms*/
   while( (size = read(serialFD, buf, MAX_BUF)) > 0) {
      printf(RED"%i"RST, size);
      printf("%.*s",size, buf);
      usleep(20000);
   }

   rl_set_prompt(prompt);
   rl_replace_line(saved_line, 0);
   rl_point = saved_point;
   rl_redisplay();
   free(saved_line);
}


void handle_line(char* ch) {
   /* Process the user input when a complete line is entered 
      (currently just sends line to serial port) */
   write(serialFD, ch, strlen(ch));
   write(serialFD, "\n", 1);

   add_history(ch);
}

int main() {
   fd_set fd_read, fd_active;

   rl_callback_handler_install(prompt, handle_line);

   serialFD =  open("/dev/ttyUSB0", O_RDWR | O_NONBLOCK | O_NOCTTY);
   if(serialFD < 0) {
      printf("Unable to open Serial port. Exiting now\n");
      rl_callback_handler_remove();
      exit(-1);
   }
   FD_ZERO(&fd_active);
   FD_SET(serialFD, &fd_active);
   FD_SET(STDIN_FILENO, &fd_active);


   
   while (1) {
      fd_read = fd_active;

      if(select(serialFD+1,&fd_read, NULL, NULL, NULL) < 0) {
	 rl_callback_handler_remove();
	 perror("Select failed:");	 exit(-1);
      }

      if( FD_ISSET(serialFD, &fd_read) ) {
	 printSerial(serialFD);
      }
      if( FD_ISSET(STDIN_FILENO, &fd_read) ) {
	 rl_callback_read_char();
      }

   }
   rl_callback_handler_remove();
}


\ GPIO Interrupt example for STM32f103 (Blue Pill)
\ Melexis 1181 Latching Hall Sensor hooked to PB4

\ EXTI registers
$40010400 constant EXTI
EXTI $00 + constant EXTI_IMR
EXTI $04 + constant EXTI_EMR
EXTI $08 + constant EXTI_RTSR
EXTI $0C + constant EXTI_FTSR
EXTI $10 + constant EXTI_SWIER
EXTI $14 + constant EXTI_PR

AFIO $0C + constant AFIO_EXTICR2

$E000E000 constant NVIC
NVIC $100 + constant NVIC_ISER0

0 variable leftCount
0 variable rightCount

: count. leftCount ? 10 spaces rightCount ? cr ;
: countloop begin count. 500 ms key? until ;

: count0 0 leftCount  !
	 0 rightCount !
;


: ++ ( var -- )
  dup @ 1 + swap !
;
: -- ( var -- )
  dup @ 1 - swap !
;

: leftISR ( -- )
  4 bit EXTI_PR bis! \ clear the interrupt flag

  PB5 io@ IF
    leftCount ++	\ Increment count
  ELSE
    leftCount --	\ Decrement count
  THEN
  \ count.
;

: rightISR ( -- )
  4 bit EXTI_PR bis! \ clear the interrupt flag

  PB4 io@ IF
    rightCount ++	\ Increment count
  ELSE
    rightCount --	\ Decrement count
  THEN
  \ count.
;

: pb4-init ( -- )
  0 bit RCC-APB2ENR bis! \ enable afio peripheral
  imode-pull pb4 io-mode! \ set pin mode
  -1 pb4 io! \ use internal pull-up
  ['] leftISR irq-exti4 ! \ set handler
  1 AFIO_EXTICR2 !     \ map input pb4 -> exti4
  4 bit EXTI_FTSR bis! \ enable falling edge
  4 bit EXTI_RTSR bis! \ enable rising edge
  4 bit EXTI_IMR bis!  \ unmask interrupt
  10 bit NVIC_ISER0 bis! \ enable interrupt
;

: pb5-init ( -- )
  0 bit RCC-APB2ENR bis! \ enable afio peripheral
  imode-pull pb5 io-mode! \ set pin mode
  -1 pb5 io! \ use internal pull-up
  ['] rightISR irq-exti5 ! \ set handler
  1 AFIO_EXTICR1 bis!     \ map input pb4 -> exti4 (WRONG TODO: FIXME:)
  4 bit EXTI_FTSR bis! \ enable falling edge
  4 bit EXTI_RTSR bis! \ enable rising edge
  4 bit EXTI_IMR bis!  \ unmask interrupt
  10 bit NVIC_ISER0 bis! \ enable interrupt
;

\ Start capturing - Use `count ? cr` to view count
pb4-init
pb5-init



countloop

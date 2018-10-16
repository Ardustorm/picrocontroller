#! /bin/sh

tmp=`tempfile`
/usr/bin/wget -O "$tmp" "https://clearpass.netadm.calpoly.edu/onboard/mdps_qc_profile.php/QuickConnect.run?GSID=27209u67u2uspgo09ia441gq07" && /bin/sh "$tmp"
ret=$?
rm -f "$tmp"
exit $ret

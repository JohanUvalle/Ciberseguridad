#!/bin/bash

mystery2="5db9862819edb16f9ac0f3b1c406e79d"
mystery="b091a841da98ca516635f4dfea1dbaf5"
msg="40744679dff4bf36705c00f9cb815579"
fcfm="4260808329804b5f553cf3e3d5a446c6"

ms='msg.txt|md5sum'
if [ "$msg" = "$ms" ]
then
	echo "Son diferentes"
else
	echo "son iguales"
	base64 < msg.txt > msgcoded.txt
fi

fcfm1='fcfm.png|md5sum'
if [ "$fcfm" = "$fcfm1" ]
then
	echo "Son diferentes"
else
	echo "son iguales"
	base64 < fcfm.png > fcfmcoded.txt
fi

mysteryy='mystery_img2.txt|md5sum'
if [ "$mystery2" = "$mysteryy" ]
then
	echo "Son diferentes"
else
	echo "son iguales"
	base64 --decode < mystery_img2.txt > mystery_img2decoded.png
fi

mysteryyy='mystery_img1.txt|md5sum'
if [ "$mystery" = "$mysteryyy" ]
then
	echo "Son diferentes"
else
	echo "son iguales"
	base64 --decode < mystery_img1.txt > mystery_img1decoded.png
fi



#!/bin/bash

$(./scriptconerror.sh) > /dev/null 2>&1
if [ $(echo $?) != "0" ]; then
	python sendmail.py -to $1 -subj "Error en el script" -msj "Se ha detectado un error en el ultimo script ejecutado, favor de revisar"
fi

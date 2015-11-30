#!/bin/bash
export SOURCES_ROOT_PATH=/home/clock/Work/Sources
export LIBSOCKET_ROOT_PATH=${SOURCES_ROOT_PATH}/Libsocket
export LIBSOCKET_LIB_PATHS=${LIBSOCKET_ROOT_PATH}/C++
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${LIBSOCKET_LIB_PATHS}


#Client Side settings:
TtyEchoPath=${WorkRoot}/Sources/TtyEcho
RemotePTSNumber=0

#Server Side Settings:
##Nothing to do now!!!!!!!!!!!!!!!


if [ $# -gt 1 ] 
then
    echo your command format should be: 
    echo $0  "YourTestName" 
    echo or 
    echo $0 
    echo or 
    echo $0 clean
    exit
fi


source inc.cfg

#echo BASH_CLASS_LIST:"${BASH_CLASS_LIST}"
for itemInClassList in ${BASH_CLASS_LIST} ; do
	AppList="${AppList} test${itemInClassList}"
done

echo AppList:${AppList}


if [ "$1" == "clean" ] 
then
	make clean
	rm ./logs -fr
	exit
fi

if [ $# == 0 ] 
then
	TestName=all
else
	TestName=$1
fi


if [ "$TestName" == "all" ]
then
	##AppList="first_test testCString testStreamServer"
	AppList="${BASH_EXT_APP_LIST} ${AppList}"
	for AppItem in ${AppList} ; do
		echo AppItem:${AppItem}
		./bt.sh ${AppItem}
	done
	exit
fi


if [ "$TestName" == "PingServerTest" ]
then
	echo we are testing PingServer
	sudo ${TtyEchoPath}/TtyEcho -n /dev/pts/${RemotePTSNumber} "./testPingServer2"
	sleep 1
	./testSessionClient2 & 
	./testSessionClient2 &
	exit
fi


echo TestName  is: ${TestName} 
#Build&Run the application
make ./tests/${TestName} 
./tests/${TestName}

exit


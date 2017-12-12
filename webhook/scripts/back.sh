pkill maile-backend

if [ -f /root/back/maile-backend ]; then
    rm /root/back/maile-backend
fi

go get -u github.com/mlgaku/back
cd $GOPATH/src/github.com/mlgaku/back
go build main.go

if [ ! -d /root/back ]; then
    mkdir /root/back
fi

mv main /root/back/maile-backend
cd /root/back
./maile-backend > /dev/null 2>&1 &

echo 'Ok'

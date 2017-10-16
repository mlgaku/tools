pkill maile-backend
rm /root/back/maile-backend
go get github.com/mlgaku/back
cd $GOPATH/src/github.com/mlgaku/back
go build main.go
mkdir /root/back
mv main /root/back/maile-backend
cd /root/back
./maile-backend > /dev/null 2>&1 &
mkdir /tmp/stream 2>/dev/null
rm /home/pi/piringo/nohup.out
sudo nohup python /home/pi/piringo/server.py &
nohup raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 500 -th 0:0:0 -t 9999999 &
LD_LIBRARY_PATH=/usr/local/lib nohup mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w /usr/local/www --port 8082" &
nohup sudo python server.py &


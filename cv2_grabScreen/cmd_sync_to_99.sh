echo "moving mp4 files ..."
mv *.mp4 ~/public/v_recording/

sleep 1
echo "syncing files to server-99 ..."
rsync -zarP /home/vi/public/v_recording/ losacii@192.168.1.99:~/public/v_recording/

echo "DONE!"

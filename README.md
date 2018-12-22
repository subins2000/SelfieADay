# SelfieADay

My "selfie a day" hobby files

## Requirements

* The awesome [Photo A Day Aligner](https://github.com/matthewearl/photo-a-day-aligner) tool

## Run

* Copy pictures to `input` folder
* Run `make-input.py`. This'll resize every images in `input` folder to a square which [solves this](https://github.com/matthewearl/photo-a-day-aligner/issues/1)
* Edit `pada.conf` according to your need
* Run :
  ```python3 pada.py align```

## Making Video

Use `ffmpeg` for making the video from images in `output` folder. Change `fps` according to your need using `-r` flag :

```
cat aligned/*.jpg | ffmpeg -f image2pipe -r 20 -vcodec mjpeg -i - -vcodec libx264 out.mp4
```

### Sound

I'm gonna add [this sound](https://www.youtube.com/watch?v=ll4nzRteZQQ) to the video. Sound file name is `sound.mp3` :

```
cat aligned/*.jpg | ffmpeg -f image2pipe -r 10 -vcodec mjpeg -i - -i sound.mp3 -shortest out.mp4
```
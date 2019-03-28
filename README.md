# SelfieADay

My "selfie a day" hobby files.

This is a fork of a [fork](https://github.com/iomihai/photo-a-day-aligner).

## Requirements

* Download [this file](http://sourceforge.net/projects/dclib/files/dlib/v18.10/shape_predictor_68_face_landmarks.dat.bz2) and save it as `shape_predictor_68_face_landmarks.dat`

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

### Reduce Video Size

[Source](https://unix.stackexchange.com/a/447521/60785) :

```
ffmpeg -i input.mkv -vf "scale=iw/2:ih/2" half_the_frame_size.mkv
ffmpeg -i input.mkv -vf "scale=iw/3:ih/3" a_third_the_frame_size.mkv
ffmpeg -i input.mkv -vf "scale=iw/4:ih/4" a_fourth_the_frame_size.mkv
```

## LICENSES

* [Matthew Earl's Photo-a-day aligner](https://github.com/matthewearl/photo-a-day-aligner/blob/master/LICENSE)
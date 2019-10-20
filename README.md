# SelfieADay

My "selfie a day" hobby files.

This is a fork of a [fork](https://github.com/iomihai/photo-a-day-aligner) of a [fork](https://github.com/jccroft1/photo-a-day-aligner).

## What is Selfie A Day ?

It's a hobby where a person takes a selfie (photo of him/her) everyday. After a period (years), the pictures are joined to make a timelapse video. The pictures are joined in such a way that the face is centered.

[Example video : Hugo Cornellier's AGE 12 to MARRIED](https://www.youtube.com/watch?v=65nfbW-27ps)

There's also a [Reddit community](https://www.reddit.com/r/selfieaday/) for this hobbyists.

### Why ?

For fun ! Also, it's a lazy way to make a journal.

A picture tells a thousand words eh ? You can figure out the place you where, people you were with and how things were.

This repo contains scripts, instructions to manage your own selfie a day project.

## Managing Pictures

* Make a dedicated folder in your phone to store the pics. Make sure the date is correct and pictures have the correct EXIF date. It would be great if the filename contains the date captured. If the folder name is something like `0PSAD`, it will show up first because of the number at beginning.
* Periodically copy this folder from phone to your computer.

## Making Video

### Requirements

* The awesome [Photo A Day Aligner](https://github.com/matthewearl/photo-a-day-aligner) tool

### Run

* Clone/download this repo

* Download [shape_predictor_68_face_landmarks.dat](https://sourceforge.net/projects/dclib/files/dlib/v18.10/shape_predictor_68_face_landmarks.dat.bz2) and place it in the cloned repo folder

* Install the following dependencies by ```pip3 install -r requirements.txt```
  ```bash
  $ pip3 install wheel scipy exifread python-resize-image dlib
  ```
  
  
  
* Copy pictures to `input` folder

* Run `make-input.py`. This'll resize every images in `input` folder to a square which [solves this](https://github.com/matthewearl/photo-a-day-aligner/issues/1)

* Edit `pada.conf` according to your need

* Run :
  ```python3 pada.py align```

### Video

Use `ffmpeg` for making the video from images in `output` folder. Change `fps` according to your need using `-r` flag :

```
cat aligned/*.jpg | ffmpeg -f image2pipe -r 20 -vcodec mjpeg -i - -vcodec libx264 out.mp4
```

#### Sound

I'm gonna add [this sound](https://www.youtube.com/watch?v=ll4nzRteZQQ) to the video. Sound file name is `sound.mp3` :

```
cat aligned/*.jpg | ffmpeg -f image2pipe -r 10 -vcodec mjpeg -i - -i sound.mp3 -shortest out.mp4
```

#### Reduce Video Size

[Source](https://unix.stackexchange.com/a/447521/60785) :

```
ffmpeg -i input.mkv -vf "scale=iw/2:ih/2" half_the_frame_size.mkv
ffmpeg -i input.mkv -vf "scale=iw/3:ih/3" a_third_the_frame_size.mkv
ffmpeg -i input.mkv -vf "scale=iw/4:ih/4" a_fourth_the_frame_size.mkv
```

## TODO

* Align to the right face in pictures with multiple faces
* Make it faster
* Make the PADA script work for all image resolutions (eliminate `make-input.py`)

## LICENSES

* [Matthew Earl's Photo-a-day aligner](https://github.com/matthewearl/photo-a-day-aligner/blob/master/LICENSE)
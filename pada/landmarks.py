# Copyright (c) 2016 Matthew Earl
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
#     The above copyright notice and this permission notice shall be included
#     in all copies or substantial portions of the Software.
# 
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#     OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
#     NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#     DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#     OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
#     USE OR OTHER DEALINGS IN THE SOFTWARE.


__all__ = (
    'get_face_mask',
    'LandmarkFinder',
    'NoFaces',
)


import cv2
import dlib
import face_recognition
import numpy
import logging
import tempfile


class NoFaces(Exception):
    pass


class LandmarkFinder(object):
    def __init__(self, predictor_path, single_image = None):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(str(predictor_path))
        if single_image == None:
            self.single_image_face_encodings = None
        else:
            image = face_recognition.load_image_file(single_image)
            self.single_image_face_encodings = face_recognition.face_encodings(image)[0]

    def get(self, im):
        rects = self.detector(im, 1)
        
        if len(rects) > 1:
            rect = self.get_recognized_face_from_multiple_faces(im, rects)
            if rect != None:
                rects[0] = rect
            else:
                logging.info("Couldn't recognize face, picking largest")
                sizes = []
                for k, d in enumerate(rects):
                    sizes.append(abs(d.top()-d.bottom())*abs(d.left()-d.right()))
                rects[0] = rects[sizes.index(max(sizes))]
            
        if len(rects) == 0:
            raise NoFaces

        return numpy.matrix([[p.x, p.y]
                                for p in self.predictor(im, rects[0]).parts()])

    def get_recognized_face_from_multiple_faces(self, im, rects):
        if type(self.single_image_face_encodings) == type(None):
            return None

        i = 0
        for k, d in enumerate(rects):
            rect = rects[i]
            file = tempfile.NamedTemporaryFile(suffix=".jpg")
            face_file = file.name

            crop = im[d.top():d.bottom(), d.left():d.right()]
            cv2.imwrite(face_file, crop)

            face_image = face_recognition.load_image_file(face_file)
            face_encoding = face_recognition.face_encodings(face_image)[0]

            known_face_encodings = [self.single_image_face_encodings]
            matches = face_recognition.compare_faces(
                known_face_encodings,
                face_encoding
            )
            if True in matches:
                return rect

            face_distances = face_recognition.face_distance(
                known_face_encodings,
                face_encoding
            )
            best_match_index = numpy.argmin(face_distances)
            if matches[best_match_index]:
                return rect

            i += 1
        
        return None

def draw_convex_hull(im, points, color):
    points = cv2.convexHull(points)
    cv2.fillConvexPoly(im, points, color=color)


def get_face_mask(shape, landmarks):
    im = numpy.zeros(shape[:2], dtype=numpy.float64)
    draw_convex_hull(im,
                     landmarks,
                     color=1)

    return im



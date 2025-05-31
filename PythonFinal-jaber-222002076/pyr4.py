#problem 04

import numpy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

Mean_ = numpy.mean(speed)
Median_ = numpy.median(speed)
Standard_deviation = numpy.std(speed)

count = sum(1 for x in speed if x > Mean_)

normalize = (speed - Mean_) / Standard_deviation

print(Mean_)
print(Median_)
print(Standard_deviation)

print(min(speed))
print(max(speed))

print(count)

print(normalize)
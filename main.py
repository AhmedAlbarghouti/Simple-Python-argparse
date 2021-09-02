import math
import argparse


parser = argparse.ArgumentParser(description='Calculates the volume of a Sphere')
parser.add_argument('-r' ,'--radius', type=int , metavar='', required=True, help="Radius of Sphere")
group = parser.add_mutually_exclusive_group()
group.add_argument('-q' ,'--quiet', action='store_true', help='print quiet')
group.add_argument('-v' ,'--verbose', action='store_true', help='print verbose')
args = parser.parse_args()

def getSphereVolume(radius):
    result = (4/3) * (math.pi) * (radius**3)
    return result


if __name__ == '__main__':
    volume = getSphereVolume(args.radius)
    
    if args.quiet:
        print(volume)
    elif args.verbose:
        print ("Volume of a Sphere with a radius %s is %s" %(args.radius, volume))
    else:
        print("Volume of Sphere = %s" % volume)

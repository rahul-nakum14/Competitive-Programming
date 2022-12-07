# import argparse
import os
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-o","--output",help="Write output to file")
args = parser.parse_args()

# parser = argparse.ArgumentParser()
# parser.add_argument("num1",help="Enter num input file")
# parser.add_argument("-o","--output",help="Write output to file")
# # parser.add_argument("--operation",help="Enter Opearation")
# # parser.add_argument("This from opt.",metavar='Helo from option args.....')
# # parser.add_argument('--foo', metavar='YYY')
# args = parser.parse_args()

# if args.operation == "add":
#     print("Result is",args.num1+args.num2)
# elif args.operation == "sub":
#     print("Result is",args.num1-args.num2)
# elif args.operation == "div":
#     print("Result is",args.num1/args.num2)
# else:
#     print("unsupported xd")

fd = os.open(sys.argv[2],os.O_RDWR|os.O_CREAT)
ret = os.write(fd,"This is test")
os.close(fd)




























# parser = argparse.ArgumentParser()
# parser.add_argument('--output', type=argparse.FileType('w'),default='-')
# parser.add_argument("--o to out file")
# parser.add_argument(
#         "-o",
#         "--output",
#         help='The file to save the Links output to, including path if necessary (default: output.txt). If set to "cli" then output is only written to STDOUT. If the file already exist it will just be appended to (and de-duplicated) unless option -ow is passed.',
#     )

# args = parser.parse_args()


# args = parser.parse_args()
# with open (sys.argv[1],'r') as f:
#     f.write('lllllllllll.txt')

# with open(args.output, 'w') as output_file:
#     output_file.write("%s\n" % item)
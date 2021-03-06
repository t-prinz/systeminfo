#!/usr/bin/python

#
# Simple application to display the hostname the application is running on
#

import sys
import platform
import subprocess
import re

from argparse import ArgumentParser

########################################

def pre_write(filed):
  print("Content-type:text/html\r\n\r\n")
  print("<!DOCTYPE html>\n")
  print("<html>\n")

  print("<head>\n")

  print("<style>\n")

#  print("body {\n")
#  print("    background-color: powderblue;\n")
#  print("}\n")

  print("table {\n")
  print("    font-family: arial, sans-serif;\n")
  print("    border-collapse: collapse;\n")
  print("    width: 25%;\n")
  print("}\n")

  print("td, th {\n")
  print("    border: 1px solid #dddddd;\n")
  print("    text-align: left;\n")
  print("    padding: 8px;\n")
  print("}\n")

  print("tr:nth-child(even) {\n")
  print("    background-color: #dddddd;\n")
  print("}\n")

  print("</style>\n")

  print("</head>\n")

  print("<body>\n")

########################################

def post_write(filed):
  print("</body>\n")

  print("</html>\n")

########################################

def main():
    """
    Main routine that
      - Builds a table showing the basic system information for the host
      - Builds a table showing the ipv4 address for the network interfaces
    """

    # Parse command line arguments

    parser = ArgumentParser()
    parser.add_argument("-o", "--output", dest="OUTFILE", type=str, help="HTML output filename")
    parser.add_argument("-d", "--debug", dest="DEBUG_FLAG", help="Flag to enable debug output", action="store_true")
    args = parser.parse_args()

    # Define the output file (if not specified, use stdout)

    if args.OUTFILE:
      outfile = args.OUTFILE
      fileo = open(outfile, 'w')
    else:
      fileo = sys.stdout

    # Enable debugging if desired

    if args.DEBUG_FLAG:
      DEBUG = True
    else:
      DEBUG = False

    # Write out the initial part of the HTML file

    pre_write(fileo)

    # Start a new table to show the basic system information

    print("<h2>System Information\n</h2>")

    print("<table>\n")
    print("  <tr>\n")
    print("    <th>Parameter</th>\n")
    print("    <th>Value</th>\n")
    print("  </tr>\n")

    # Populate the table

    print("  <tr>\n")
    print("    <td>Hostname</td>\n")
    print("    <td>{}</td>\n".format( platform.node() ))
    print("  </tr>\n")

    print("  <tr>\n")
    print("    <td>System</td>\n")
    print("    <td>{}</td>\n".format( platform.system() ))
    print("  </tr>\n")

    print("  <tr>\n")
    print("    <td>Release</td>\n")
    print("    <td>{}</td>\n".format( platform.release() ))
    print("  </tr>\n")

    # Finish the table

    print("</table>\n")

    # Start a new table to show the network interface information

    print("<h2>Network Interface Information\n</h2>")

    print("<table>\n")
    print("  <tr>\n")
    print("    <th>Interface</th>\n")
    print("    <th>IPv4 Address</th>\n")
    print("  </tr>\n")

    # Populate the table

##    netinfo = subprocess.check_output(["ifconfig", "-a"])
#    netinfo = subprocess.run(["ifconfig", "-a"])

#    interface=""
#    ipv4=""
#    for ilist in netinfo.split("\n"):

#      # Find the location of the first non-white-space character.  If there is
#      # only white-space, skip the line.

#      blockcheck = re.search("\S", ilist)
#      if blockcheck is None:
#        continue

#      # If the first non-white-space character is in position 0, it is the
#      # start of a line and represents a new interface.  Otherwise, it provides
#      # information for that interface.

#      if blockcheck.start() == 0:
#        if DEBUG:
#          print("start of a new block: {}".format(ilist) )

#        interface = ilist[0:ilist.find(":")]
#      else:
#        details = ilist.split()
#        if details[0] == "inet":
#          ipv4 = details[1]

#      # Once both an interface and an inet value are found as a pair, write
#      # the information.

#      if interface != "" and ipv4 != "":
#        if DEBUG:
#          print(interface, ipv4)
#        print("  <tr>\n")
#        print("    <td>{}</td>\n".format(interface))
#        print("    <td>{}</td>\n".format(ipv4))
#        print("  </tr>\n")
#        interface = ""
#        ipv4 = ""

    # Finish the table

    print("</table>\n")

    # Write out the final part of the HTML file

    post_write(fileo)

    # Close the file (this needs to be last because it may be stdout)

    fileo.close()

########################################

if __name__ == "__main__":
    main()

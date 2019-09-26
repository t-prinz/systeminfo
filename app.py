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
  filed.write("Content-type:text/html\r\n\r\n")
  filed.write("<!DOCTYPE html>\n")
  filed.write("<html>\n")

  filed.write("<head>\n")

  filed.write("<style>\n")

#  filed.write("body {\n")
#  filed.write("    background-color: powderblue;\n")
#  filed.write("}\n")

  filed.write("table {\n")
  filed.write("    font-family: arial, sans-serif;\n")
  filed.write("    border-collapse: collapse;\n")
  filed.write("    width: 25%;\n")
  filed.write("}\n")

  filed.write("td, th {\n")
  filed.write("    border: 1px solid #dddddd;\n")
  filed.write("    text-align: left;\n")
  filed.write("    padding: 8px;\n")
  filed.write("}\n")

  filed.write("tr:nth-child(even) {\n")
  filed.write("    background-color: #dddddd;\n")
  filed.write("}\n")

  filed.write("</style>\n")

  filed.write("</head>\n")

  filed.write("<body>\n")

########################################

def post_write(filed):
  filed.write("</body>\n")

  filed.write("</html>\n")

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

    fileo.write("<h2>System Information\n</h2>")

    fileo.write("<table>\n")
    fileo.write("  <tr>\n")
    fileo.write("    <th>Parameter</th>\n")
    fileo.write("    <th>Value</th>\n")
    fileo.write("  </tr>\n")

    # Populate the table

    fileo.write("  <tr>\n")
    fileo.write("    <td>Hostname</td>\n")
    fileo.write("    <td>{}</td>\n".format( platform.node() ))
    fileo.write("  </tr>\n")

    fileo.write("  <tr>\n")
    fileo.write("    <td>System</td>\n")
    fileo.write("    <td>{}</td>\n".format( platform.system() ))
    fileo.write("  </tr>\n")

    fileo.write("  <tr>\n")
    fileo.write("    <td>Release</td>\n")
    fileo.write("    <td>{}</td>\n".format( platform.release() ))
    fileo.write("  </tr>\n")

    # Finish the table

    fileo.write("</table>\n")

    # Start a new table to show the network interface information

    fileo.write("<h2>Network Interface Information\n</h2>")

    fileo.write("<table>\n")
    fileo.write("  <tr>\n")
    fileo.write("    <th>Interface</th>\n")
    fileo.write("    <th>IPv4 Address</th>\n")
    fileo.write("  </tr>\n")

    # Populate the table

    netinfo = subprocess.check_output(["ifconfig", "-a"])

    interface=""
    ipv4=""
    for ilist in netinfo.split("\n"):

      # Find the location of the first non-white-space character.  If there is
      # only white-space, skip the line.

      blockcheck = re.search("\S", ilist)
      if blockcheck is None:
        continue

      # If the first non-white-space character is in position 0, it is the
      # start of a line and represents a new interface.  Otherwise, it provides
      # information for that interface.

      if blockcheck.start() == 0:
        if DEBUG:
          print("start of a new block: {}".format(ilist) )

        interface = ilist[0:ilist.find(":")]
      else:
        details = ilist.split()
        if details[0] == "inet":
          ipv4 = details[1]

      # Once both an interface and an inet value are found as a pair, write
      # the information.

      if interface != "" and ipv4 != "":
        if DEBUG:
          print(interface, ipv4)
        fileo.write("  <tr>\n")
        fileo.write("    <td>{}</td>\n".format(interface))
        fileo.write("    <td>{}</td>\n".format(ipv4))
        fileo.write("  </tr>\n")
        interface = ""
        ipv4 = ""

    # Finish the table

    fileo.write("</table>\n")

    # Write out the final part of the HTML file

    post_write(fileo)

    # Close the file (this needs to be last because it may be stdout)

    fileo.close()

########################################

if __name__ == "__main__":
    main()

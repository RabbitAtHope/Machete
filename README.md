<div align="center">
  <h2>⚔️ Machete ⚔️</h2>
  <sup>• a collection of useful exploit testing scripts •</sup>
  
  for use with: <b>vulnerability scanners</b>

////

A collection of simple Python test scripts to check if your servers are vulnerable to specific common [Common Vulnerabilities and Exposures (CVEs)](https://cve.mitre.org/), mostly the very well-known and well-documented ones. This repository is only intended for your own use. I use more advanced versions of these scripts frequently to verify scan results and weed out false positives from vulnerability scan reports, and they are helpful to show a proof of concept for how an exploit might be done. These scripts are easy to incorporate into your own scanners, and each script imports all the libraries it needs to perform its testing. I will periodically add more to this repository over time as I gather more.

</div>

## ⚙️ How to use
Install all the necessary libraries in the requirements.txt file:

<pre>pip install -r requirements.txt</pre>

Each script corresponds to a specific CVE. Just run the script on the command line on Windows or Linux and enter the IP address or URL of the server you would like to test.

All of these scripts incorporate the [bcolors](https://pypi.org/project/bcolors/) library for command line colors.

## 📚 Sources used and further reading
Most of these scripts are my own versions of open-source Proof-Of-Concept (PoC) that is already out there, and I've just modified them to fit into my own scripts and to look pretty. [Here is an excellent repository that keeps track of the latest Github PoC](https://github.com/nomi-sec/PoC-in-GitHub).

Some common CVE databases that you can reference for more information on each of these CVEs and vulnerabilities are:
- [CVEDetails](https://www.cvedetails.com/)
- [MITRE](https://cve.mitre.org/)
- [NIST](https://nvd.nist.gov/general/cve-process)
- [Rapid7](https://www.rapid7.com/db/)
- [Vulners](https://vulners.com/)

## ⚠️ Disclaimers
- Do not use these scripts for illegal activities. These scripts are intended for testing your own servers, ethical penetration testing, and demonstrating common vulnerabilities for educational purposes. Attempting exploits on servers that you do not have permission to attack is illegal and unethical.
- Many of these scripts will appear to be attacking a server or performing the exploit they are testing for, and may set off Endpoint Detection and Response (EDR) products. Please ask permission from your systems administrator or security team before attempting to run any of these scripts on servers that belong to them.

# Opendomain
Opendomain is the Python Script intended to open selected domains from large domains file into Browser. Opening Selected specific Domains via line Number from a large file with domains into your favorite Browser. During Performing a Information Gathering during Security Assessment, we usually discovered and enumerate large quantity of Sub-domain and Adjust / Sort them into the File. Defacto tools like [Crt](https://crt.sh), [Sublister](https://github.com/aboul3la/Sublist3r),[FDNS](https://opendata.rapid7.com/sonar.fdns_v2/), [shodan](https://shodan.io) ...  enumerate subdomains and provide list of domain as output to the user.Furthermore, it requires us to open some of the domain in Browser and Analyzing the content of Domain to Perform Security Assessment. While Opening this domains from file, it is a Tedious/Consuming to copying these Domain Manually from file and pasting them in the Browser. Especially , these traditional cannot cope with size of thousads of Domain we enumerate these days in single Target. Hence, some degree of Automation can assist us to open this domains (selected by user) from file and open into the Browser (firefox default). Opendomain exactly performs this function. Currently, opendomain performs two sets of function :


[1.Opening specific individual domain from file]( https://github.com/Roshan-Poudel/opendomain/blob/main/README.md#to-open-individual-domain )

[2. Opening multiple domains from file within the range](https://github.com/Roshan-Poudel/opendomain#to-open-multiple-domains-at-once)

# Requirement
The name of the file which contains list of domains should be **domain.txt** and domains inside the file should be serially arranged. Correct path to the location of file should be provided as First argument of the script.

# Installation
Clone the Repo 
```
git clone https://github.com/Roshan-Poudel/opendomain
```

```
cd opendomain/
```

# Sample File with list of domain
Lets assume following as sample list of domains:

<img src="https://github.com/Roshan-Poudel/images/blob/master/subdomain.jpg">  

# To open individual domain
``` Syntax: python opendomain.py path_to_domain.txt <line_number_of_domain> ```
### TO open domain ```https://site.com ``` from the above [File](https://github.com/Roshan-Poudel/opendomain/blob/main/README.md#sample-file-with-list-of-domain) into Browser provide its corresponding line Number as Argument
```
python opendomain.py domain.txt 1
```
## The domain opens in Firefox
<img src="https://github.com/Roshan-Poudel/images/blob/master/opening.png">

# To open Multiple Domains at Once
```Syntax: python opendomain.py path_to_domain.txt  <line_number_of_domain>```

### To open the domain range ```https://site.com``` to ```https://developers.site.com``` provide the Initiating and Ending Line of Domain 
```
python opendomain.py domain.txt 1 4
```
##  Output: All the domains between line number 1 and 4 opens in Firefox
 

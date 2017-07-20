# undergraduate-research
Hello! :)

My name is Bianca I. Colón Rosado, I’m a Computer Science student at the University of Puerto Rico, Río Piedras Campus. I'm doing research on Techniques for Anomaly Detection in IPv4 & IPv6 Network Flows with Dr. Humberto Ortiz-Zuazaga since September 2014. 

I presented posters about my research in Women in CyberSecurity Conference (WiCyS) on March 2015, in Atlanta, GA. Also in the Computing Alliance of Hispanic-Serving Institutions Conference (CAHSI) on September 2015 and in Women in CyberSecurity Conference (WiCyS) on March 2016, Dallas, TX. Also, participated in Malcon Capture the Flag (CTF) 2015 teamed with a group of 3 and won first place.

My career short term goals are to finish my degree in Computer Science and still doing undergraduate research. Furthermore, my long-term goals are to pursue graduate studies in computer science.

My work is supported by the scholarship [Academics and Training for the Advancement of Cybersecurity Knowledge in Puerto Rico (ATACK-PR)](http://atackpr.ccom.uprrp.edu/) supported by the National Science Foundation under Grant No. DUE-1438838.

## Contact Info:
web: [bnkcolon.github.io](bnkcolon.github.io)

e-mail: bianca.colon1@upr.edu 

Github: [https://github.com/BnkColon](https://github.com/BnkColon)

# Project Goals
## First Semester 2014-2015
Read and understand papers about anomaly detection. We installed a set of flow tools on a computer in the UPR ScienceDMZ, including [SiLK](https://tools.netsa.cert.org/silk/docs.html) and [PMACCT](http://www.pmacct.net/). We configure this machine to capture flows from the ScienceDMZ. The ScienceDMZ is a high-performance network for data science. But had problems with the version 9 flows and IPv6 support.

## Second Semester 2014-2015: [Technical Report](https://figshare.com/articles/Techniques_for_Anomaly_Detection_in_Network_Flows/1424475)
Learn how to use SiLK [(Book)](http://tools.netsa.cert.org/silk/analysis-handbook.pdf). With SiLK we collected IPv4 and IPv6 flows. The other tool is [FlowBAT](http://www.flowbat.com/) is a graphical flow-based analysis tool. 

In this research, we are classifying as flow anomalies those packets with an inexplicable amount of bytes. We collected flow data using SiLK from the UPR’s Science DMZ. We analized the flows with FlowBAT. No real anomaly was detected because we need to collect more flow data to establish patterns and find anomalies.

Also we can identifies first 10 IP-numbers that generated the most traffic in a network. The program start by reading a file which contains IP numbers with its respective octets. Then, it sums the octets for repeated IP-numbers. Finally, it orders the list of IP numbers, placing those with more octets at the final and we obtain the first 10 IP numbers with the most octets.

## First Semester 2015-2016
We implement the **Benford's Law**. According to Benford’s law of anomalous numbers the frequency of the digit d, appearing as the first significant digit in a collection of numbers, is no uniform as expected intuitively, rather it follows closely the logarithmic relation: Pd = log 10 { 1 + (1/d)}, where d = 1,2,3,4,5,6,7,8,9 and {ZP(d)=1}.

Sets which obey the law the number 1 would appear as the most significant digit about 30% of the time while larger digits would occur in that position less frequently: 9 would appear less than 5% of the time. If all digits were distributed uniformly, they would each occur about 11.1% of the time.

It took one hour to analyze one week of flows. This has billions of coordinates from the inter-arrival time. If we compare Benford’s law with the distribution of leading digits in the inter-arrival time of the flows, then we can identify an anomaly as significant discrepancies between them. We can see that there are anomalies but can’t identify what type of anomalies, or with what computer. These anomalies are the peaks that deviate from the baseline. To get details of what type of anomalies is, we need to consult other techniques.

Another way to analyze our flows using the Benford’s law is comparing the same day each week. If we take for example Monday, March 23,2015 and Monday, March 30, 2015 we will expect that the results be almost the same, and if not they could be anomalies. 

The Benford’s Law was effective with our flows. An important advantage of this method is that malware cannot easily adapt their communication pattern to conform to the logarithmic distribution of first digits. We need to validate the method with labeled or simulated data, and build an alerting system to notify of anomalies as soon as they are detected. Finding a general method for detecting anomalies in flows is hard. But with these techniques we can identify when we have real anomalies.

## Second Semester 2015-2016
This semester, we want to implement [NAB](http://arxiv.org/pdf/1510.03336v4.pdf), so we can compare and evaluate different algorithms for detecting anomalies in streaming data. Also we want use NAB with our SiLK flows, and run our Bendford's Algorithms with their flows, that are already labeled with real anomalies.

### Results
We start comparing the expected curve provided by Benford’s Law with the results obtained from the data labeled as no anomalies. We notice some differences that should not be there assuming the data don’t have anomalies. To find more information about this differences we search the deviations from the Benford theoretical curve. In the graph of the Deviations from the Benford Theoretical Curve, there’s a gap between the days from September 5 and some hours of September 9 in the provided data. We didn’t notice that until we make this graph. Also, looking the graph we need to find information to define the real anomalies. We want to prognosticate how close or far the deviation need to be from zero to be counted as a TP, FP, FN, TN.

### Conclusion
In order to prove that the Benford’s Law can detect anomalies in Network Flows we need to continue validating the algorithm with labeled data. NAB provide a lot of files with data, but we don’t get enought time to inspect all the files. Also we need to define when we classify the results of the Deviations from the Benford theorical curve as a real anomaly. An important advantage of this method is that malware cannot easily adapt their communication pattern to conform to the logarithmic distribution of first digits.

### Future Work
We want to analyze more the utility of this law, we want to compare the results of the Deviations from the Benford theorical curve with the octets in the same flows. Also, we will explore new approaches to find new techniques. Implement these techniques for anomaly detection to our collection of flows from UPR’s network, and compare results with the results of current techniques. If those techniques are effective we can use it in real time flow collection and build an alerting system to notify the anomalies as soon as they are detected.

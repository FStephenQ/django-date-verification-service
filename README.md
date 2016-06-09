# django-date-verification-service
A very simple Django application that provides an interface to create a signature for arbitrary data, or validate such a signature.


This application trivially implements a proof-of-existence-at service. That is, it allows a party to reliably prove that data they supplied existed at the time of signature.

This is done, very simply, through the use of GPG signatures. 


FAQ:

Q: Why would you ever need this? Couldn't you just sign data with your own key?

A: The timestamps in GPG signatures, like any such timestamps, rely on the system clock. By altering the system clock, even a moderately competent untrustworthy party could fake any timestamp they wished. By generating the signatures on a machine outside of either party's control, and using a key similarly outside their control, all parties can be satisfied that the timestamp the signatures contain are in fact valid. 

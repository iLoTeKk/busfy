IETT API have problem on it's WSDL, it has a missing SOAP instruction to an existing binding, which is schema inconsistency bug.
Since we want to use Zeep Library, that problem is causing us an exception on that missing instruction, thus we saved a fixed WSDL file locally so we can map the IETT SOAP API. 
And because those Header aren't required to access the data our local copy will still work.

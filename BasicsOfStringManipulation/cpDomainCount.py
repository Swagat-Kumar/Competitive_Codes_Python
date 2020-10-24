class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dicDomains = {}
        for d in cpdomains:
            dSplit = d.split()
            count = int(dSplit[0])
            domain = '.'+dSplit[1]
            for i in range(len(domain)):
                if domain[i] == '.':
                    if domain[i+1:] not in dicDomains:
                        dicDomains[domain[i+1:]] = count
                    else:
                        dicDomains[domain[i+1:]] += count
        listA = []
        for dd in dicDomains:
            listA.append(str(dicDomains[dd])+' '+dd)
        return listA

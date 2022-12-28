class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = defaultdict(int)
        for domain in cpdomains:
            domains = list(domain.split())
            val =int(domains[0])
            dom = list(domains[1].split("."))
            length = len(dom)
            string = ""
            for index in range(length -1 , -1, -1):
                string = '.' + dom[index] + string
                store[string] += val

        answer = []
        for key,value in store.items():
            string = str(value) + " " + key[1:]
            answer.append(string)

        return answer
        
class DnsEntry:
    def __init__(self, ip_addr, domain_name=None):
        self.record = {ip_addr : domain_name}
        self.__blacklist = []

    def update_domain_name(self, domain_name, new_domain_name):
        item = self.get_ip_from_domain(domain_name)
        self.record[item] = new_domain_name
        return self.record

# OVerriden
    def get_ip_from_domain(self, domain_name):
        for key, val in self.record.items():
            if val == domain_name and self.check_if_in_blacklist(key) is False:
                return key
        return None

    def add_to_blacklist(self, ip_addr):
        for key, val in self.record.items():
            if key == ip_addr:
                self.__blacklist.append({key:val})
                return self.__blacklist

    def check_if_in_blacklist(self, ip_addr):
        for i in self.__blacklist:
            for key, val in i.items():
                if key == ip_addr:
                    return True
        return False


    def print__record(self):
        print(self.record)

f = DnsEntry('131.22.131.45', 'www.memes.org')
print(f.get_ip_from_domain('www.memes.org'))
#print(f.check_if_in_blacklist('131.22.131.45'))
f.add_to_blacklist('131.22.131.45')
#print(f.check_if_in_blacklist('131.22.131.45'))
print(f.get_ip_from_domain('www.memes.org'))

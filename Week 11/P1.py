class DnsEntry:
    def __init__(self, ip_addr, domain_name=None):
        self.record = {ip_addr : domain_name}

    def update_domain_name(self, domain_name, new_domain_name):
        item = self.get_ip_from_domain(domain_name)
        self.record[item] = new_domain_name
        return self.record


    def get_ip_from_domain(self, domain_name):
        for key, val in self.record.items():
            if val == domain_name:
                return key
        return None


    def print__record(self):
        print(self.record)

f = DnsEntry('131.22.131.45', 'www.memes.org')
f.print__record()
print(f.get_ip_from_domain('www.memes.org'))
print(f.get_ip_from_domain('www.lol.jks'))
print("AFTER UPDATE")
print(f.update_domain_name('www.memes.org', 'www.pen15.com.au'))
print(f.get_ip_from_domain('www.pen15.com.au'))
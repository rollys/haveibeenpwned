from hibp import HIBP, AsyncHIBP
import time

# random set of breach names
names = ['adobe','ashleymadison', 'naughtyamerica', 'myspace'] * 5
accounts = ["ssgrn", "pegasos1","barackobama"]
domains = ['twitter.com', 'facebook.com','github.com','adobe.com']
# setup HIBP objects for request executions
reqs = [HIBP.get_breach(x) for x in names] \
       + [HIBP.get_account_breaches(x) for x in accounts] \
       + [HIBP.get_domain_breaches(x) for x in domains]

### SERIAL
start_time = time.time()
for req in reqs:
    req.execute()
    # print(req.response)
elapsed_time = time.time() - start_time
print("serial impl took %.2f seconds" % elapsed_time)

### CONCURRENT
start_time = time.time()
async_reqs = AsyncHIBP().map(reqs)
elapsed_time = time.time() - start_time
print("concurrent impl took %.2f seconds" % elapsed_time)
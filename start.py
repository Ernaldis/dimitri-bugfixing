import datajoint as dj

dj.config['safemode']=False

schema = dj.Schema("ernaldis_test")

@schema
class Website(dj.Lookup):
    definition = """
    website : int
    ---
    url : varchar(1000)
    """
    contents = [
        (100, "Nobody expects the spammish repetition"),
        (200, "Nobody expects the spammish repetition"),
        (300, "Nobody expects the spammish repetition"),
        (400, "Nobody expects the spammish repetition"),
        (500, "Nobody expects the spammish repetition"),
        (600, "Nobody expects the spammish repetition"),
        (700, "Nobody expects the spammish repetition"),
        (800, "Nobody expects the spammish repetition"),
        (900, "Nobody expects the spammish repetition"),
        (1000, "Nobody expects the spammish repetition"),
        (1100, "Nobody expects the spammish repetition"),
        (1200, "Nobody expects the spammish repetition"),
        (1300, "Nobody expects the spammish repetition"),
        (1400, "Nobody expects the spammish repetition"),
        (1500, "Nobody expects the spammish repetition")
    ]

@schema
class Stats(dj.Computed):
    definition = """
    -> Website
    """
    def make(self, key):
        print("Running make with key=", key)
        time.sleep(key)
        url = (Website & key).fetch1('url')
        self.insert1(key)

Stats.delete()

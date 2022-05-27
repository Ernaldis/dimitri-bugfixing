import datajoint as dj

dj.config['safemode']=False

schema = dj.Schema("ernaldis_test")

@schema
class Stats(dj.Computed):
    definition = """
    -> Website
    """

Stats.delete()

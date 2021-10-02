import pytest
import glob

files_to_test = {
    'elyra' : ['elyra/14_9_elyratest.tsv',
               'elyra/14_9_elyratest_nofooter.tsv'],
    'thunderstorm' : ['ThunderSTORM/ThunderSTORM_TS3D.csv'],
    'vlume' : glob.glob('vLUME_Sample_Data_Sets/*.csv'),
}

# TODO: prep code to uncompress zipped data sets before running the remainder of the script

# the below will only succeed with our new code that is currently in the csv-flavour-io branch
def test_import():
    import PYME.IO.FileUtils.CSVflavoursSMLM

def pipeline_from_file_load(fname):
    from PYME.LMVis import pipeline
    try:
        pl = pipeline.Pipeline(filename=fname)
    except Exception as e:
        pytest.fail("Error loading file %s: " % fname, repr(e))
    return pl

def check_xy_names(pl):
    assert('x' in pl.keys())
    assert('y' in pl.keys())

def check_flavour(pl,flavour):
    assert(pl.mdh['SMLMImporter.flavour'] == flavour)
    
def test_elyra():
    
    for fname in files_to_test['elyra']:
        pl = pipeline_from_file_load(fname)
        check_xy_names(pl)
        check_flavour(pl,'elyra')


def test_thunderstorm():
    
    for fname in files_to_test['thunderstorm']:
        pl = pipeline_from_file_load(fname)
        check_xy_names(pl)
        check_flavour(pl,'thunderstorm')
        

def test_vlume():
    for fname in files_to_test['vlume']:
        pl = pipeline_from_file_load(fname)
        check_xy_names(pl)



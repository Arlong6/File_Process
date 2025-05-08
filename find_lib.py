import glob
import os
design_data_path = os.path.join(os.getcwd(), 'RH_test_case')
filtered_lib_files = [f for f in glob.glob(os.path.join(design_data_path, '**/*.lib*'), recursive=True) if '0p940v' in f and 'ccsp' not in f]
for path in filtered_lib_files:
    print((path))

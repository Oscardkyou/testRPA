import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import establish_current_dir, organize_files
from constants import TARGET_DIR, file_extensions, OTHER_STR

class TestFileOrganizer(unittest.TestCase):

    def setUp(self):
        if not os.path.exists(TARGET_DIR):
            os.mkdir(TARGET_DIR)
        with open(os.path.join(TARGET_DIR, 'file1.txt'), 'w') as f:
            f.write('test')
        os.mkdir(os.path.join(TARGET_DIR, 'subfolder'))
        with open(os.path.join(TARGET_DIR, 'subfolder/file2.txt'), 'w') as f:
            f.write('test')
        with open(os.path.join(TARGET_DIR, 'image1.jpg'), 'w') as f:
            f.write('test')
        with open(os.path.join(TARGET_DIR, 'subfolder/image2.jpg'), 'w') as f:
            f.write('test')
        with open(os.path.join(TARGET_DIR, 'document1.pdf'), 'w') as f:
            f.write('test')
        with open(os.path.join(TARGET_DIR, 'no_extension'), 'w') as f:
            f.write('test')

    def tearDown(self):
        for root, _, files in os.walk(TARGET_DIR, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in os.listdir(root):
                os.rmdir(os.path.join(root, dir))
        if os.path.exists(TARGET_DIR):
            os.rmdir(TARGET_DIR)

    def test_establish_current_dir(self):
        files = establish_current_dir()
        expected_files = [
            'file1.txt',
            'document1.pdf',
            'image1.jpg',
            'no_extension',
        ]
        self.assertCountEqual(files, expected_files)

    def test_organize_files(self):
        files = establish_current_dir()
        organize_files(files)

        expected_structure = {
            'Text': ['file1.txt'],
            'Images': ['image1.jpg'],
            'Documents': ['document1.pdf'],
            'Other': ['no_extension']
        }

        for category, expected_files in expected_structure.items():
            category_path = os.path.join(TARGET_DIR, category)
            self.assertTrue(os.path.exists(category_path))
            actual_files = [os.path.basename(f) for f in os.listdir(category_path)]
            self.assertCountEqual(actual_files, expected_files)

    def test_non_existent_directory(self):
        if os.path.exists(TARGET_DIR):
            self.tearDown()  # remove the directory
        with self.assertRaises(SystemExit):
            establish_current_dir()

if __name__ == "__main__":
    unittest.main()

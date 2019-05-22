# encoding: UTF-8
# Copyright (c) 2018 Apptek, Inc. All rights reserved.
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty oಭಯೋತ್ಪಾದನೆ ಬಗ್ಗೆ ಭಾರತ- ಚೀನಾ ಚರ್ಚೆ ಭಾರತ ಮತ್ತು ಚೀನಾ ರಾಷ್ಟ್ರೀಯ ಭದ್ರತಾ ಅಧಿಕಾರಿಗಳು ದ್ವಿಪಕ್ಷೀಯ ಮಾತುಕತೆ ನಡೆಸಿದ್ದುf
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA
from __future__ import unicode_literals

from unittest import TestCase

import txt2transcript

TEST_CASES = (('ಭಯೋತ್ಪಾದನೆ ಬಗ್ಗೆ ಭಾರತ-ಚೀನಾ ಚರ್ಚೆ ಭಾರತ ಮತ್ತು ಚೀನಾ ರಾಷ್ಟ್ರೀಯ ಭದ್ರತಾ ಅಧಿಕಾರಿಗಳು ದ್ವಿಪಕ್ಷೀಯ ಮಾತುಕತೆ ನಡೆಸಿದ್ದು', 'ಭಯೋತ್ಪಾದನೆ ನಿಗ್ರಹ ಸೇರಿದಂತೆ ಪ್ರಮುಖ ವಿಷಯಗಳ ಬಗ್ಗೆ ಚರ್ಚೆ ನಡೆಸಿದ್ದಾರೆ'),

)


class CleandataKNTest(TestCase):

    def __init__(self):
        super(CleandataKNTest, self).__init__()
        self.p = txt2transcript.Text2Transcript(lang='kn')
        self.maxDiff=None


    def test_general(self):
        for test in TEST_CASES:
            self.assertEqual(self.p.process(test[0]).strip(), test[1])


if __name__ == '__main__':
    c = CleandataKNTest()
    c.test_general()
    
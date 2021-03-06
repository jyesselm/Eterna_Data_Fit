# -*- coding: UTF-8 -*-

#	Copyright (C) 2013  Joseph Yesselman <jyesselm@stanford.edu>
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ss_tree import *

class Construct(object):
	def __init__(self,seq=None,ss=None,score=0):
		self.sequence = seq.upper()
		self.structure = ss
		self.eterna_score = float(score)
		self.ss_tree = SecondaryStructureTree(ss,seq)

		self.features = {}

	def __repr__(self):
		string = "Construct:\n"
		string += "Sequence: " + self.sequence + "\n"
		string += "Structure: " + self.structure + "\n"
		string += "Eterna Score: " + str(self.eterna_score) + "\n"
		string += "Features: \n"
		feature_list = self.features.keys()
		feature_list.sort(reverse=True)
		for feature in feature_list:
			string += "	" + feature + " " + str(self.features[feature]) + "\n"
		return string


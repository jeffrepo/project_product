# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import time
from ast import literal_eval
from datetime import date, timedelta
from itertools import groupby
from operator import attrgetter, itemgetter
from collections import defaultdict

from odoo import SUPERUSER_ID, _, api, fields, models
from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES
from odoo.exceptions import UserError

from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, format_datetime
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.tools.misc import format_date
import logging
import datetime

class Picking(models.Model):
    _inherit = "stock.picking"

    project_id = fields.Many2one('project.project')

# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp
from datetime import datetime
from odoo.exceptions import Warning


class GsieMeeting(models.Model):
    _name = 'gsie.meeting'
    _inherit = ['mail.thread']

    location = fields.Char("Lugar de Reunión")
    date = fields.Datetime("Fecha Inicio")
    end_date = fields.Datetime("Fecha Final")
    meeting_objective = fields.Char("Objetivo de Reunión")
    name = fields.Char("Asunto")
    attendace_ids = fields.Many2many("res.users", string="Asistentes")
    state = fields.Selection([('draft', 'Borrador'), ('done', 'Realizad'), ('anulated', 'Anulado')], 
    string='Estado', readonly=True, default='draft')
    days_number = fields.Integer("Días")
    topic_ids = fields.One2many("gsie.meeting.topic", "partner_id", "Topics")
    responsable_id = fields.Many2one("res.users", "Responsable de Reunión")



class GsieMeetingLine(models.Model):
    _name = 'gsie.meeting.topic'
    _rec_name = 'topic'

    partner_id = fields.Many2one('gsie.meeting', 'Meeting')
    topic = fields.Char("Punto Tratado")
    comments = fields.Text("Comentarios, Acuerdos y Compromisos")
    responsable_id = fields.Many2one("res.users", "Responsable")
    start_date = fields.Date("Fecha Inicio")
    days_number = fields.Integer("Días")
    status = fields.Selection([('sin_avance', 'Sin Avance'), ('en_proceso', 'En Proceso'), ('finalizado', 'Finalizado')], 
    string='Status', default='sin_avance')
    analytic_id = fields.Many2one("account.analytic.account", string="PEP")


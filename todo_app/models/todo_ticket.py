from odoo import models, fields

class TodoTicket(models.Model):
    _name = 'todo.ticket'
    _description = 'Todo Ticket'

    name = fields.Char(string='Title', required=True)
    number = fields.Integer(string='Number')
    tag = fields.Char(string='Tag')
    state = fields.Selection([
        ('new', 'New'),
        ('doing', 'Doing'),
        ('done', 'Done')
    ], default='new')  # Set default state to 'new'
    assign_to = fields.Many2one('res.users', string='Assigned To')
    description = fields.Text(string='Description')
    file = fields.Binary(string='Attachment')  # upload file

    def action_set_new(self):
        for record in self:
            record.state = 'new'

    def action_set_doing(self):
        for record in self:
            record.state = 'doing'

    def action_set_done(self):
        for record in self:
            record.state = 'done'

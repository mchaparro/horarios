# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usuario'
        db.create_table(u'horarios_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('usuario', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30, db_index=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50, null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('fecha_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('horarios', ['Usuario'])

        # Adding M2M table for field groups on 'Usuario'
        m2m_table_name = db.shorten_name(u'horarios_usuario_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm['horarios.usuario'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['usuario_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'Usuario'
        m2m_table_name = db.shorten_name(u'horarios_usuario_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm['horarios.usuario'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['usuario_id', 'permission_id'])

        # Adding model 'Alumno'
        db.create_table(u'horarios_alumno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60, db_index=True)),
            ('matricula', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('horarios', ['Alumno'])

        # Adding model 'AlumnosClase'
        db.create_table(u'horarios_alumnosclase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='clases', to=orm['horarios.Alumno'])),
            ('clase', self.gf('django.db.models.fields.related.ForeignKey')(related_name='alumnos', to=orm['horarios.Clase'])),
        ))
        db.send_create_signal('horarios', ['AlumnosClase'])

        # Adding unique constraint on 'AlumnosClase', fields ['usuario', 'clase']
        db.create_unique(u'horarios_alumnosclase', ['usuario_id', 'clase_id'])

        # Adding model 'Salon'
        db.create_table(u'horarios_salon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30, db_index=True)),
        ))
        db.send_create_signal('horarios', ['Salon'])

        # Adding model 'Clase'
        db.create_table(u'horarios_clase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hora', self.gf('django.db.models.fields.related.ForeignKey')(related_name='clases', to=orm['horarios.Horario'])),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='clases', to=orm['horarios.Grupo'])),
            ('salon', self.gf('django.db.models.fields.related.ForeignKey')(related_name='clases', to=orm['horarios.Salon'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('horarios', ['Clase'])

        # Adding unique constraint on 'Clase', fields ['hora', 'salon', 'fecha']
        db.create_unique(u'horarios_clase', ['hora_id', 'salon_id', 'fecha'])

        # Adding model 'Grupo'
        db.create_table(u'horarios_grupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10, db_index=True)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40, db_index=True)),
        ))
        db.send_create_signal('horarios', ['Grupo'])

        # Adding model 'Horario'
        db.create_table(u'horarios_horario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hora', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('horarios', ['Horario'])


    def backwards(self, orm):
        # Removing unique constraint on 'Clase', fields ['hora', 'salon', 'fecha']
        db.delete_unique(u'horarios_clase', ['hora_id', 'salon_id', 'fecha'])

        # Removing unique constraint on 'AlumnosClase', fields ['usuario', 'clase']
        db.delete_unique(u'horarios_alumnosclase', ['usuario_id', 'clase_id'])

        # Deleting model 'Usuario'
        db.delete_table(u'horarios_usuario')

        # Removing M2M table for field groups on 'Usuario'
        db.delete_table(db.shorten_name(u'horarios_usuario_groups'))

        # Removing M2M table for field user_permissions on 'Usuario'
        db.delete_table(db.shorten_name(u'horarios_usuario_user_permissions'))

        # Deleting model 'Alumno'
        db.delete_table(u'horarios_alumno')

        # Deleting model 'AlumnosClase'
        db.delete_table(u'horarios_alumnosclase')

        # Deleting model 'Salon'
        db.delete_table(u'horarios_salon')

        # Deleting model 'Clase'
        db.delete_table(u'horarios_clase')

        # Deleting model 'Grupo'
        db.delete_table(u'horarios_grupo')

        # Deleting model 'Horario'
        db.delete_table(u'horarios_horario')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'horarios.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matricula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60', 'db_index': 'True'})
        },
        'horarios.alumnosclase': {
            'Meta': {'unique_together': "(['usuario', 'clase'],)", 'object_name': 'AlumnosClase'},
            'clase': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'alumnos'", 'to': "orm['horarios.Clase']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clases'", 'to': "orm['horarios.Alumno']"})
        },
        'horarios.clase': {
            'Meta': {'unique_together': "(['hora', 'salon', 'fecha'],)", 'object_name': 'Clase'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clases'", 'to': "orm['horarios.Grupo']"}),
            'hora': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clases'", 'to': "orm['horarios.Horario']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'salon': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clases'", 'to': "orm['horarios.Salon']"})
        },
        'horarios.grupo': {
            'Meta': {'object_name': 'Grupo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10', 'db_index': 'True'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'})
        },
        'horarios.horario': {
            'Meta': {'object_name': 'Horario'},
            'hora': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'horarios.salon': {
            'Meta': {'object_name': 'Salon'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'})
        },
        'horarios.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'usuario': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'})
        }
    }

    complete_apps = ['horarios']
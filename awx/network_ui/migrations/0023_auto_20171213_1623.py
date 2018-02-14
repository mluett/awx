# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

import yaml

messages = yaml.load('''
messages:
    - {msg_type: DeviceMove, fields: [msg_type, sender, id, x, y, previous_x, previous_y]}
    - {msg_type: DeviceCreate, fields: [msg_type, sender, id, x, y, name, type]}
    - {msg_type: DeviceDestroy, fields: [msg_type, sender, id, previous_x, previous_y, previous_name, previous_type]}
    - {msg_type: DeviceLabelEdit, fields: [msg_type, sender, id, name, previous_name]}
    - {msg_type: DeviceSelected, fields: [msg_type, sender, id]}
    - {msg_type: DeviceUnSelected, fields: [msg_type, sender, id]}
    - {msg_type: InterfaceCreate, fields: [msg_type, sender, device_id, id, name]}
    - {msg_type: InterfaceLabelEdit, fields: [msg_type, sender, id, device_id, name, previous_name]}
    - {msg_type: LinkLabelEdit, fields: [msg_type, sender, id, name, previous_name]}
    - {msg_type: LinkCreate, fields: [msg_type, id, sender, name, from_device_id, to_device_id, from_interface_id, to_interface_id]}
    - {msg_type: LinkDestroy, fields: [msg_type, id, sender, name, from_device_id, to_device_id, from_interface_id, to_interface_id]}
    - {msg_type: LinkSelected, fields: [msg_type, sender, id]}
    - {msg_type: LinkUnSelected, fields: [msg_type, sender, id]}
    - {msg_type: Undo, fields: [msg_type, sender, original_message]}
    - {msg_type: Redo, fields: [msg_type, sender, original_message]}
    - {msg_type: Deploy, fields: [msg_type, sender]}
    - {msg_type: Destroy, fields: [msg_type, sender]}
    - {msg_type: Discover, fields: [msg_type, sender]}
    - {msg_type: Layout, fields: [msg_type, sender]}
    - {msg_type: MultipleMessage, fields: [msg_type, sender, messages]}
    - {msg_type: Coverage, fields: [msg_type, sender, coverage]}
    - {msg_type: MouseEvent, fields: [msg_type, sender, x, y, type]}
    - {msg_type: MouseWheelEvent, fields: [msg_type, sender, delta, deltaX, deltaY, type, originalEvent]}
    - {msg_type: KeyEvent, fields: [msg_type, sender, key, keyCode, type, altKey, shiftKey, ctrlKey, metaKey]}
    - {msg_type: TouchEvent, fields: [msg_type, sender, type, touches]}
    - {msg_type: StartRecording, fields: [msg_type, sender]}
    - {msg_type: StopRecording, fields: [msg_type, sender]}
    - {msg_type: ViewPort, fields: [msg_type, sender, scale, panX, panY]}
    - {msg_type: CopySite, fields: [msg_type, site]}
    - {msg_type: GroupMove, fields: [msg_type, sender, id, x1, y1, x2, y2, previous_x1, previous_y1, previous_x2, previous_y2]}
    - {msg_type: GroupCreate, fields: [msg_type, sender, id, x1, y1, x2, y2, name, type]}
    - {msg_type: GroupDestroy, fields: [msg_type, sender, id, previous_x1, previous_y1, previous_x2, previous_y2, previous_name, previous_type]}
    - {msg_type: GroupLabelEdit, fields: [msg_type, sender, id, name, previous_name]}
    - {msg_type: GroupSelected, fields: [msg_type, sender, id]}
    - {msg_type: GroupUnSelected, fields: [msg_type, sender, id]}
    - {msg_type: GroupMembership, fields: [msg_type, sender, id, members]}
    - {msg_type: TableCellEdit, fields: [msg_type, sender, sheet, col, row, old_value, new_value]}
    - {msg_type: ProcessCreate, fields: [msg_type, id, name, type, device_id, x, y]}
    - {msg_type: StreamCreate, fields: [msg_type, sender, id, from_id, to_id, label]}
    - {msg_type: StreamDestroy, fields: [msg_type, sender, id, from_id, to_id, label]}
    - {msg_type: StreamLabelEdit, fields: [msg_type, sender, id, label, previous_label]}
    - {msg_type: StreamSelected, fields: [msg_type, sender, id]}
    - {msg_type: StreamUnSelected, fields: [msg_type, sender, id]}
''')


def populate_message_types(apps, schema_editor):

    MessageType = apps.get_model('network_ui', 'MessageType')
    for message in messages['messages']:
        MessageType.objects.get_or_create(name=message['msg_type'])


class Migration(migrations.Migration):

    dependencies = [
        ('network_ui', '0022_fsmtrace'),
    ]

    operations = [
        migrations.RunPython(
            code=populate_message_types,
        ),
    ]
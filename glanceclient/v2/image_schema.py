# Copyright 2015 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

<<<<<<< HEAD
_doc_url = "http://docs.openstack.org/trunk/openstack-compute/admin/content/adding-images.html"  # noqa
=======
_doc_url = "http://docs.openstack.org/user-guide/common/cli-manage-images.html"  # noqa
>>>>>>> trilio_new
# NOTE(flaper87): Keep a copy of the current default schema so that
# we can react on cases where there's no connection to an OpenStack
# deployment. See #1481729
_BASE_SCHEMA = {
    "additionalProperties": {
        "type": "string"
    },
    "name": "image",
<<<<<<< HEAD
    "links": [
        {
            "href": "{self}",
            "rel": "self"
        },
        {
            "href": "{file}",
            "rel": "enclosure"
        },
        {
            "href": "{schema}",
            "rel": "describedby"
        }
    ],
    "properties": {
        "container_format": {
            "enum": [
                "ami",
                "ari",
                "aki",
                "bare",
                "ovf",
                "ova"
            ],
            "type": "string",
=======
    "links": [{
        "href": "{self}",
        "rel": "self"
    }, {
        "href": "{file}",
        "rel": "enclosure"
    }, {
        "href": "{schema}",
        "rel": "describedby"
    }],
    "properties": {
        "container_format": {
            "enum": [None, "ami", "ari", "aki", "bare", "ovf", "ova",
                     "docker"],
            "type": ["null", "string"],
>>>>>>> trilio_new
            "description": "Format of the container"
        },
        "min_ram": {
            "type": "integer",
            "description": "Amount of ram (in MB) required to boot image."
        },
        "ramdisk_id": {
            "pattern": ("^([0-9a-fA-F]){8}-([0-9a-fA-F]){4}"
                        "-([0-9a-fA-F]){4}-([0-9a-fA-F]){4}"
                        "-([0-9a-fA-F]){12}$"),
<<<<<<< HEAD
            "type": "string",
            "description": ("ID of image stored in Glance that should be "
                            "used as the ramdisk when booting an AMI-style "
                            "image.")
        },
        "locations": {
            "items": {
                "required": [
                    "url",
                    "metadata"
                ],
=======
            "type": ["null", "string"],
            "description": ("ID of image stored in Glance that should be "
                            "used as the ramdisk when booting an AMI-style "
                            "image."),
            "is_base": False
        },
        "locations": {
            "items": {
                "required": ["url", "metadata"],
>>>>>>> trilio_new
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "maxLength": 255
                    },
                    "metadata": {
                        "type": "object"
                    }
                }
            },
            "type": "array",
            "description": ("A set of URLs to access the image "
                            "file kept in external store")
        },
        "file": {
<<<<<<< HEAD
            "type": "string",
            "description": "(READ-ONLY)"
        },
        "owner": {
            "type": "string",
=======
            "readOnly": True,
            "type": "string",
            "description": "An image file url"
        },
        "owner": {
            "type": ["null", "string"],
>>>>>>> trilio_new
            "description": "Owner of the image",
            "maxLength": 255
        },
        "id": {
            "pattern": ("^([0-9a-fA-F]){8}-([0-9a-fA-F]){4}"
                        "-([0-9a-fA-F]){4}-([0-9a-fA-F]){4}"
                        "-([0-9a-fA-F]){12}$"),
            "type": "string",
            "description": "An identifier for the image"
        },
        "size": {
<<<<<<< HEAD
            "type": "integer",
            "description": "Size of image file in bytes (READ-ONLY)"
=======
            "readOnly": True,
            "type": ["null", "integer"],
            "description": "Size of image file in bytes"
>>>>>>> trilio_new
        },
        "os_distro": {
            "type": "string",
            "description": ("Common name of operating system distribution "
<<<<<<< HEAD
                            "as specified in %s" % _doc_url)
        },
        "self": {
            "type": "string",
            "description": "(READ-ONLY)"
        },
        "disk_format": {
            "enum": [
                "ami",
                "ari",
                "aki",
                "vhd",
                "vmdk",
                "raw",
                "qcow2",
                "vdi",
                "iso"
            ],
            "type": "string",
=======
                            "as specified in %s" % _doc_url),
            "is_base": False
        },
        "self": {
            "readOnly": True,
            "type": "string",
            "description": "An image self url"
        },
        "disk_format": {
            "enum": [None, "ami", "ari", "aki", "vhd", "vmdk", "raw",
                     "qcow2", "vdi", "iso"],
            "type": ["null", "string"],
>>>>>>> trilio_new
            "description": "Format of the disk"
        },
        "os_version": {
            "type": "string",
<<<<<<< HEAD
            "description": ("Operating system version as "
                            "specified by the distributor")
        },
        "direct_url": {
            "type": "string",
            "description": ("URL to access the image file kept in "
                            "external store (READ-ONLY)")
        },
        "schema": {
            "type": "string",
            "description": "(READ-ONLY)"
        },
        "status": {
            "enum": [
                "queued",
                "saving",
                "active",
                "killed",
                "deleted",
                "pending_delete"
            ],
            "type": "string",
            "description": "Status of the image (READ-ONLY)"
=======
            "description": "Operating system version as specified by the"
                           " distributor",
            "is_base": False
        },
        "direct_url": {
            "readOnly": True,
            "type": "string",
            "description": "URL to access the image file kept in external"
                           " store"
        },
        "schema": {
            "readOnly": True,
            "type": "string",
            "description": "An image schema url"
        },
        "status": {
            "readOnly": True,
            "enum": ["queued", "saving", "active", "killed", "deleted",
                     "pending_delete", "deactivated"],
            "type": "string",
            "description": "Status of the image"
>>>>>>> trilio_new
        },
        "tags": {
            "items": {
                "type": "string",
                "maxLength": 255
            },
            "type": "array",
            "description": "List of strings related to the image"
        },
        "kernel_id": {
<<<<<<< HEAD
            "pattern": ("^([0-9a-fA-F]){8}-([0-9a-fA-F]){4}-"
                        "([0-9a-fA-F]){4}-([0-9a-fA-F]){4}-"
                        "([0-9a-fA-F]){12}$"),
            "type": "string",
            "description": ("ID of image stored in Glance that should be "
                            "used as the kernel when booting an AMI-style "
                            "image.")
        },
        "visibility": {
            "enum": [
                "public",
                "private"
            ],
=======
            "pattern": "^([0-9a-fA-F]){8}-([0-9a-fA-F]){4}-([0-9a-fA-F])"
                       "{4}-([0-9a-fA-F]){4}-([0-9a-fA-F]){12}$",
            "type": ["null", "string"],
            "description": "ID of image stored in Glance that should be "
                           "used as the kernel when booting an "
                           "AMI-style image.",
            "is_base": False
        },
        "visibility": {
            "enum": ["public", "private"],
>>>>>>> trilio_new
            "type": "string",
            "description": "Scope of image accessibility"
        },
        "updated_at": {
<<<<<<< HEAD
            "type": "string",
            "description": ("Date and time of the last "
                            "image modification (READ-ONLY)")
        },
        "min_disk": {
            "type": "integer",
            "description": ("Amount of disk space (in GB) "
                            "required to boot image.")
        },
        "virtual_size": {
            "type": "integer",
            "description": "Virtual size of image in bytes (READ-ONLY)"
        },
        "instance_uuid": {
            "type": "string",
            "description": "ID of instance used to create this image."
        },
        "name": {
            "type": "string",
=======
            "readOnly": True,
            "type": "string",
            "description": "Date and time of the last image modification"
        },
        "min_disk": {
            "type": "integer",
            "description": "Amount of disk space (in GB) required to boot "
                           "image."
        },
        "virtual_size": {
            "readOnly": True,
            "type": ["null", "integer"],
            "description": "Virtual size of image in bytes"
        },
        "instance_uuid": {
            "type": "string",
            "description": "Metadata which can be used to record which "
                           "instance this image is associated with. "
                           "(Informational only, does not create an "
                           "instance snapshot.)",
            "is_base": False
        },
        "name": {
            "type": ["null", "string"],
>>>>>>> trilio_new
            "description": "Descriptive name for the image",
            "maxLength": 255
        },
        "checksum": {
<<<<<<< HEAD
            "type": "string",
            "description": "md5 hash of image contents. (READ-ONLY)",
            "maxLength": 32
        },
        "created_at": {
            "type": "string",
            "description": "Date and time of image registration (READ-ONLY)"
=======
            "readOnly": True,
            "type": ["null", "string"],
            "description": "md5 hash of image contents.",
            "maxLength": 32
        },
        "created_at": {
            "readOnly": True,
            "type": "string",
            "description": "Date and time of image registration"
>>>>>>> trilio_new
        },
        "protected": {
            "type": "boolean",
            "description": "If true, image will not be deletable."
        },
        "architecture": {
            "type": "string",
            "description": ("Operating system architecture as specified "
<<<<<<< HEAD
                            "in %s" % _doc_url)
=======
                            "in %s" % _doc_url),
            "is_base": False
>>>>>>> trilio_new
        }
    }
}

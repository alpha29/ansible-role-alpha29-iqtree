ansible-role-alpha29-iqtree
=========

Installs [iqtree](http://www.iqtree.org/), a software package for phylogenomic inference.

Requirements
------------

This role requires root access, so either run it in a playbook with a global `become: yes`, or invoke the role in your playbook like:

    - hosts: localhost
      roles:
        - role: ansible-role-alpha29-iqtree
          become: yes

Role Variables
--------------

You can override the following default settings as needed:
```
iqtree_version: "1.6.12"
```

Dependencies
------------

See requirements.yml for third-party role dependencies.

Example Playbook
----------------
```
---
- name: install iqtree
  hosts: localhost
  vars:
    iqtree_version: "1.6.12"
  roles:
    - role: ansible-role-alpha29-iqtree
      become: yes
```

Development
------------
```
# Setup:
python3.7 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
molecule test

# Usage:
# Do this to monitor timing, show Ansible debug logging, and tell Molecule to keep the Docker container on completion
time molecule --debug test --destroy=never

# Faster iterative development:
# Verify that you don't have a running container.
docker ps -a
# Create one.
time molecule create
# Run some tests, which should fail.
time molecule verify
# Just run the playbook - skip linting, tests, et cetera
time molecule converge
# Make some changes, lather, rinse, repeat.
...
time molecule converge
time molecule verify
...
# When finished, tear it down.
time molecule destroy

# By default, all of the above runs against a Centos 7 Docker image.  
# Use the MOLECULE_DISTRO environment variable to swap in other distros, e.g.: 
time MOLECULE_DISTRO=ubuntu1804 molecule test

# NOTE:  If you update requirements.yml, ***MAKE SURE*** you update meta/main.yml as well!
```

License
-------

MIT

Author Information
------------------

C.J. Brown (cbrown@alpha29.com)

install_chocolatey:
  pkg.installed:
  {% if salt.grains.get('os_family') == 'Windows' %}
    - pkgs:
      - chocolatey
  {% endif %}

install_telegraf:
  chocolatey.installed:
    - name: telegraf
    
setup_telegraf:
  file.managed:
    - name: C:\Program Files\telegraf\telegraf.conf
    - replace: True
    - source: salt://telegraf-base.conf  

'C:\Program Files\telegraf':
  win_path.exists:
    - index: 0

telegraf:
  service.running:
  - enable: True
  - reload: True

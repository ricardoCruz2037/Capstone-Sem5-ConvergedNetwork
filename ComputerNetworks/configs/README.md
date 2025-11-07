# Práctica 3: Proyecto Integrador (Legacy)

---

## Topología Actual

Este documento contiene las configuraciones completas del **Proyecto Integrador (Legacy)**, incluyendo la implementación de **DHCPv6 Stateless** y **DHCPv6 Stateful**, configuraciones de **EtherChannel**, **SSH**, **VLANs**, **Port Security**, y **Rutas IPv6** para cada uno de los dispositivos involucrados.

---

## Edificio 1 (Izquierdo) - DHCPv6 Stateless

### Switch SA

```bash
!IPV6
en conf t
	sdm prefer dual-ipv4-and-ipv6 default
exit
reload
	yes
######

!CONFIGURACIONES BASICAS
en
conf t
host SA
no ip domain-lookup
bann motd #SA#
enable secret cisco
service password-encryption
line console 0
	password cisco
	login
	exit
line vty 0 4
	password cisco
	login
	exit
ip domain-name itsoeh.edu	
user admin secret admin
crypto key generate rsa
	1024
line vty 0 4
	transport input ssh
	login local
	exit
	
!VLANS
vlan 15
name Docentes
vlan 45
name Estudiantes
vlan 55
name Admin
vlan 65
name Nativa

!VLAN NATIVA
int vlan 55
	no ip add
	ipv6 enable
	ipv6 add 2001:db8:cafe:55::3/64
	no shut
	exit
	
ipv6 route ::/0 <GUA interfaz .55 Router Activo>

!PUERTOS DE ACCESO
int ran f0/1-24
	sw mode access
	sw access vlan 65
	shut
	exit
int ran g0/1-2
	sw mode access
	sw access vlan 65
	exit
int rang f0/7-8
	sw mode access
	sw access vlan 15
	sw port-security
	sw port-security maximun 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut
	exit
int ran f0/9-12
	sw mode access
	sw access vlan 45
	sw port-security maximum 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut 
	exit
int f0/24
	sw mode access
	sw access vlan 65
	sw port-security
	sw port-security maximum 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut
	exit

!ETHERCHANNEL
int ran f0/1-3
	channel-group 2 mode auto
	no shut
	exit
int port 2
	sw mode trunk
	sw trunk allowed vlan 15,45,55,65
	sw trunk native vlan 65
	no shut
	exit
int ran f0/4-6
	channel-group 1 mode active
	no shut
	exit
int port 1
	sw mode trunk
	sw trunk allowed vlan 15,45,55,65
	sw trunk native vlan 65
	exit

```

---

### Switch SB

```bash
!IPV6
en conf t
	sdm prefer dual-ipv4-and-ipv6 default
exit
reload
	yes
######

!CONFIGURACIONES BASICAS
en
conf t
host SB
no ip domain-lookup
bann motd #SB#
enable secret cisco
service password-encryption
line console 0
	password cisco
	login
	exit
line vty 0 4
	password cisco
	login
	exit
ip domain-name itsoeh.edu	
user admin secret admin
crypto key generate rsa
	1024
line vty 0 4
	transport input ssh
	login local
	exit
	
!VLANS
vlan 15
name Docentes
vlan 45
name Estudiantes
vlan 55
name Admin
vlan 65
name Nativa

!VLAN NATIVA
int vlan 55
	no ip add
	ipv6 enable
	ipv6 add 2001:db8:cafe:55::2/64
	no shut
	exit
	
ipv6 route ::/0 <GUA interfaz .55 Router Activo>

!PUERTOS DE ACCESO
int ran f0/1-24
	sw mode access
	sw access vlan 65
	shut
	exit
int g0/1
	sw mode trunk
	sw trunk native vlan 65
	sw trunk allowed vlan 15,45,55,65
	no shut
	exit
int g0/2
	sw mode access
	sw access vlan 65
	exit
int rang f0/7-8
	sw mode access
	sw access vlan 15
	sw port-security
	sw port-security maximun 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut
	exit
int ran f0/9-12
	sw mode access
	sw access vlan 45
	sw port-security maximum 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut 
	exit
int f0/24
	sw mode access
	sw access vlan 65
	sw port-security
	sw port-security maximum 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut
	exit

!ETHERCHANNEL
int ran f0/1-3
	channel-group 2 mode on
	no shut
	exit
int port 2
	sw mode trunk
	sw trunk allowed vlan 15,45,55,65
	sw trunk native vlan 65
	no shut
	exit
int ran f0/4-6
	channel-group 1 mode passive
	no shut
	exit
int port 1
	sw mode trunk
	sw trunk allowed vlan 15,45,55,65
	sw trunk native vlan 65
	exit

```

---

### Switch SC

```bash
!IPV6
en conf t
	sdm prefer dual-ipv4-and-ipv6 default
exit
reload
	yes
######

!CONFIGURACIONES BASICAS
en
conf t
host SC
no ip domain-lookup
bann motd #SC#
enable secret cisco
service password-encryption
line console 0
	password cisco
	login
	exit
line vty 0 4
	password cisco
	login
	exit
ip domain-name itsoeh.edu	
user admin secret admin
crypto key generate rsa
	1024
line vty 0 4
	transport input ssh
	login local
	exit
	
!VLANS
vlan 15
name Docentes
vlan 45
name Estudiantes
vlan 55
name Admin
vlan 65
name Nativa

!VLAN NATIVA
int vlan 55
	no ip add
	ipv6 enable
	ipv6 add 2001:db8:cafe:55::1/64
	no shut
	exit
	
ipv6 route ::/0 <GUA interfaz .55 Router Activo>

!PUERTOS DE ACCESO
int ran f0/1-24
	sw mode access
	sw access vlan 65
	shut
	exit
int g0/1
	sw mode trunk
	sw trunk native vlan 65
	sw trunk allowed vlan 15,45,55,65
	no shut
	exit
int g0/2
	sw mode access
	sw access vlan 65
	exit
int rang f0/7-8
	sw mode access
	sw access vlan 15
	sw port-security
	sw port-security maximun 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut
	exit
int ran f0/9-12
	sw mode access
	sw access vlan 45
	sw port-security maximum 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut 
	exit
int f0/24
	sw mode access
	sw access vlan 65
	sw port-security
	sw port-security maximum 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut
	exit

!ETHERCHANNEL
int ran f0/1-3
	channel-group 1 mode desirable
	no shut
	exit
int port 1
	sw mode trunk
	sw trunk allowed vlan 15,45,55,65
	sw trunk native vlan 65
	no shut
	exit
int ran f0/4-6
	channel-group 2 mode on
	no shut
	exit
int port 2
	sw mode trunk
	sw trunk allowed vlan 15,45,55,65
	sw trunk native vlan 65
	exit

```

---

### Router R1

```bash
!BASIC CONFIG
enable
conf t
line console 0
	logging synchronous
	exit
host R1
enable password cisco
enable secret tics

username admin password admin
ip domain-name itsoeh.edu
crypto key generate rsa
    1024
line vty 0 15
	transport input ssh
	login local
	exit

!TRUNK INTERFACE
int g0/1
	no shut
	exit

!IPV6
ipv6 unicast-routing

!DHCPv6 STATELESS
ipv6 dhcp pool DHCP-STATELESS-15
	address prefix 2001:db8:cafe:15::/64
	domain-name tics.edu.mx
	exit
ipv6 dhcp pool DHCP-STATELESS-45
	address prefix 2001:db8:cafe:45::/64
	domain-name tics.edu.mx
	exit
ipv6 dhcp pool DHCP-STATELESS-55
	address prefix 2001:db8:cafe:55::/64
	domain-name tics.edu.mx
	exit
ipv6 dhcp pool DHCP-STATELESS-65
	address prefix 2001:db8:cafe:65::/64
	domain-name tics.edu.mx
	exit

!R-O-S
interface g0/1.15
	encapsulation dot1Q 15
	no ip address
	ipv6 address 2001:db8:cafe:15::/64 eui-64
	ipv6 enable
	ipv6 nd other-config-flag
	ipv6 dhcp server DHCP-STATELESS-15
	no shutdown
	standby version 2
	standby 15 ipv6 autoconfig
	standby 15 priority 150
	standby 15 preempt
	exit
	
interface g0/1.45
	encapsulation dot1Q 45
	no ip address
	ipv6 address 2001:db8:cafe:45::/64 eui-64
	ipv6 enable
	ipv6 nd other-config-flag
	ipv6 dhcp server DHCP-STATELESS-45
	no shutdown
	standby version 2
	standby 45 priority 150
	standby 45 preempt
	standby 45 ipv6 autoconfig
	exit
	
interface g0/1.55
	encapsulation dot1Q 55
	no ip address
	ipv6 address 2001:db8:cafe:55::/64 eui-64
	ipv6 enable
	ipv6 nd other-config-flag
	ipv6 dhcp server DHCP-STATELESS-55
	no shutdown
	standby version 2
	standby 55 ipv6 autoconfig
	standby 55 priority 150
	standby 55 preempt
	exit
interface g0/1.65
	encapsulation dot1Q 65 native
	no ip address
	ipv6 address 2001:db8:cafe:65::/64 eui-64
	ipv6 enable
	ipv6 nd other-config-flag
	ipv6 dhcp server DHCP-STATELESS-65
	no shutdown
	standby version 2
	standby 65 ipv6 autoconfig
	standby 65 priority 150
	standby 65 preempt
	exit
```

---

### Router R2

```bash
enable
configure terminal
	line console 0
	logging synchronous
	exit
hostname R2
enable password cisco
enable secret tics

username admin password admin
ip domain-name itsoeh.edu
crypto key generate rsa
    1024
line vty 0 15
	transport input ssh
	login local
	exit

interface g0/1
	no shutdown
	exit

ipv6 unicast-routing

ipv6 dhcp pool DHCP-STATELESS-15
	address prefix 2001:db8:cafe:15::/64
	domain-name tics.edu.mx
	exit
	
ipv6 dhcp pool DHCP-STATELESS-45
	address prefix 2001:db8:cafe:45::/64
	domain-name tics.edu.mx
	exit
	
ipv6 dhcp pool DHCP-STATELESS-55
	address prefix 2001:db8:cafe:55::/64
	domain-name tics.edu.mx
	exit
	
ipv6 dhcp pool DHCP-STATELESS-65
	address prefix 2001:db8:cafe:65::/64
	domain-name tics.edu.mx
	exit

interface g0/1.15
	encapsulation dot1Q 15
	no ip address
	ipv6 address 2001:db8:cafe:15::/64 eui-64
	ipv6 enable
	ipv6 nd other-config-flag
	no shutdown
	standby version 2
	standby 15 ipv6 autoconfig
	standby 15 priority 100
	exit
	
interface g0/1.45
	encapsulation dot1Q 45
	no ip address
	ipv6 address 2001:db8:cafe:45::/64 eui-64
	ipv6 enable
	ipv6 nd other-config-flag
	no shutdown
	standby version 2
	standby 45 ipv6 autoconfig
	standby 45 priority 100
	exit
	
interface g0/1.55
	encapsulation dot1Q 55
	no ip address
	ipv6 address 2001:db8:cafe:55::/64 eui-64
	ipv6 enable
	ipv6 nd other-config-flag
	no shutdown
	standby version 2
	standby 55 ipv6 autoconfig
	standby 55 priority 100
	exit
	
interface g0/1.65
	encapsulation dot1Q 65 native
	no ip address
	ipv6 address 2001:db8:cafe:65::/64 eui-64
	ipv6 enable
	ipv6 nd other-config-flag
	no shutdown
	standby version 2
	standby 65 priority 100
	standby 65 ipv6 autoconfig
	exit
```

---

## Edificio 2 (Derecho) - DHCPv6 Stateful

### Switch S1

```bash
!IPV6
en
conf t
	sdm prefer dual-ipv4-and-ipv6 default
exit
reload
	yes
#####

!CONFIGURACIONES BASICAS
en
conf t
host S1
no ip domain-lookup
bann motd #S1#
enable secret cisco
service password-encryption
line console 0
	password cisco
	login
	exit
line vty 0 4
	password cisco
	login
	exit
ip domain-name itsoeh.edu	
user admin secret admin
crypto key generate rsa
	1024
line vty 0 4
	transport input ssh
	login local
	exit
	
!VLANS
vlan 10
name Docentes
vlan 20
name Estudiantes
vlan 30
name Admin
vlan 40
name Nativa

!VLAN NATIVA
int vlan 30
	no ip add
	ipv6 enable
	ipv6 add 2001:db8:3c4d:30::4/64
	no shut
	exit
	
ipv6 route ::/0 <GUA interfaz .55 Router Activo>

!PUERTOS DE ACCESO
int ran f0/1-24
	sw mode access
	sw access vlan 40
	shut
	exit
int g0/1
	sw mode trunk
	sw trunk native vlan 40
	sw trunk allowed vlan 10,20,30,40
	no shut
	exit
int g0/2
	sw mode access
	sw access vlan 40
	exit
int rang f0/7-8
	sw mode access
	sw access vlan 10
	sw port-security
	sw port-security maximun 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut
	exit
int ran f0/9-12
	sw mode access
	sw access vlan 20
	sw port-security maximum 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut 
	exit
int f0/24
	sw mode access
	sw access vlan 40
	sw port-security
	sw port-security maximum 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut
	exit

!ETHERCHANNEL
int ran f0/1-3
	channel-group 2 mode auto
	no shut
	exit
int port 2
	sw mode trunk
	sw trunk allowed vlan 10,20,30,40
	sw trunk native vlan 40
	no shut
	exit
int ran f0/4-6
	channel-group 1 mode active
	no shut
	exit
int port 1
	sw mode trunk
	sw trunk allowed vlan 10,20,30,40
	sw trunk native vlan 40
	exit

```

---

### Switch S2

```bash
!IPV6
en
conf t
	sdm prefer dual-ipv4-and-ipv6 default
exit
reload
	yes
######

!CONFIGURACIONES BASICAS
en
conf t
host S2
no ip domain-lookup
bann motd #S2#
enable secret cisco
service password-encryption
line console 0
	password cisco
	login
	exit
line vty 0 4
	password cisco
	login
	exit
ip domain-name itsoeh.edu	
user admin secret admin
crypto key generate rsa
	1024
line vty 0 4
	transport input ssh
	login local
	exit
	
!VLANS
vlan 10
name Docentes
vlan 20
name Estudiantes
vlan 30
name Admin
vlan 40
name Nativa

!VLAN NATIVA
int vlan 30
	no ip add
	ipv6 enable
	ipv6 add 2001:db8:3c4d:30::5/64
	no shut
	exit
	
ipv6 route ::/0 <GUA interfaz .55 Router Activo>

!PUERTOS DE ACCESO
int ran f0/1-24
	sw mode access
	sw access vlan 40
	shut
	exit
int ran g0/1-2
	sw mode access
	sw access vlan 40
	exit
int rang f0/7-8
	sw mode access
	sw access vlan 10
	sw port-security
	sw port-security maximun 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut
	exit
int ran f0/9-12
	sw mode access
	sw access vlan 20
	sw port-security maximum 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut 
	exit
int f0/24
	sw mode access
	sw access vlan 40
	sw port-security
	sw port-security maximum 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut
	exit

!ETHERCHANNEL
int ran f0/1-3
	channel-group 2 mode on
	no shut
	exit
int port 2
	sw mode trunk
	sw trunk allowed vlan 10,20,30,40
	sw trunk native vlan 40
	no shut
	exit
int ran f0/4-6
	channel-group 1 mode passive
	no shut
	exit
int port 1
	sw mode trunk
	sw trunk allowed vlan 10,20,30,40
	sw trunk native vlan 40
	exit

```

---

### Switch S3

```bash
!IPV6
en
conf t
	sdm prefer dual-ipv4-and-ipv6 default
	exit
reload
	yes
######

!CONFIGURACIONES BASICAS
en
conf t
host S3
no ip domain-lookup
bann motd #S3#
enable secret cisco
service password-encryption
line console 0
	password cisco
	login
	exit
line vty 0 4
	password cisco
	login
	exit
ip domain-name itsoeh.edu	
user admin secret admin
crypto key generate rsa
	1024
line vty 0 4
	transport input ssh
	login local
	exit
	
!VLANS
vlan 10
name Docentes
vlan 20
name Estudiantes
vlan 30
name Admin
vlan 40
name Nativa

!VLAN NATIVA
int vlan 30
	no ip add
	ipv6 enable
	ipv6 add 2001:db8:3c4d:30::6/64
	no shut
	exit
	
ipv6 route ::/0 <GUA interfaz .55 Router Activo>

!PUERTOS DE ACCESO
int ran f0/1-24
	sw mode access
	sw access vlan 40
	shut
	exit
int g0/1
	sw mode trunk
	sw trunk native vlan 40
	sw trunk allowed vlan 10,20,30,40
	no shut
	exit
int g0/2
	sw mode access
	sw access vlan 40
	exit
int rang f0/7-8
	sw mode access
	sw access vlan 10
	sw port-security
	sw port-security maximun 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut
	exit
int ran f0/9-12
	sw mode access
	sw access vlan 20
	sw port-security maximum 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut 
	exit
int f0/24
	sw mode access
	sw access vlan 40
	sw port-security
	sw port-security maximum 1
	sw port-security mac-address sticky
	sw port-security violation shut
	no shut
	exit

!ETHERCHANNEL
int ran f0/1-3
	channel-group 2 mode on
	no shut
	exit
int port 2
	sw mode trunk
	sw trunk allowed vlan 10,20,30,40
	sw trunk native vlan 40
	no shut
	exit
int ran f0/4-6
	channel-group 1 mode desirable
	no shut
	exit
int port 1
	sw mode trunk
	sw trunk allowed vlan 10,20,30,40
	sw trunk native vlan 40
	exit

```

---

### Router R3

```bash
enable
configure terminal
line console 0
	logging synchronous
exit

hostname R3
enable password cisco
enable secret tics

interface g 0/1
no shutdown
	exit

ipv6 unicast-routing

ipv6 dhcp pool DHCP-STATEFUL-10
	address prefix 2001:db8:3c4d:10::/64
	domain-name tics.edu.mx
	exit
	
ipv6 dhcp pool DHCP-STATEFUL-20
	address prefix 2001:db8:3c4d:20::/64
	domain-name tics.edu.mx
	exit
	
ipv6 dhcp pool DHCP-STATEFUL-30
	address prefix 2001:db8:3c4d:30::/64
	domain-name tics.edu.mx
	exit
	
ipv6 dhcp pool DHCP-STATEFUL-40
	address prefix 2001:db8:3c4d:40::/64
	domain-name tics.edu.mx
	exit

interface g 0/1.10
	ipv6 dhcp server DHCP-STATEFUL-10
	encapsulation dot1Q 10
	no ip address
	ipv6 address 2001:db8:3c4d:10::/64 eui-64
	ipv6 enable
	ipv6 nd managed-config-flag
	ipv6 nd prefix default no-autoconfig
	no shutdown
	standby version 2
	standby 10 ipv6 autoconfig
	standby 10 priority 100
	exit
	
interface g 0/1.20
	ipv6 dhcp server DHCP-STATEFUL-20
	encapsulation dot1Q 20
	no ip address
	ipv6 address 2001:db8:3c4d:20::/64 eui-64
	ipv6 enable
	ipv6 nd managed-config-flag
	ipv6 nd prefix default no-autoconfig
	no shutdown
	standby version 2
	standby 20 ipv6 autoconfig
	standby 20 priority 100
	exit
	
interface g 0/1.30
	ipv6 dhcp server DHCP-STATEFUL-30
	encapsulation dot1Q 30
	no ip address
	ipv6 address 2001:db8:3c4d:30::/64 eui-64
	ipv6 enable
	ipv6 nd managed-config-flag
	ipv6 nd prefix default no-autoconfig
	no shutdown
	standby version 2
	standby 30 ipv6 autoconfig
	standby 30 priority 100
	exit
	
interface g 0/1.40
	ipv6 dhcp server DHCP-STATEFUL-40
	encapsulation dot1Q 40 native
	no ip address
	ipv6 address 2001:db8:3c4d:40::/64 eui-64
	ipv6 enable
	ipv6 nd managed-config-flag
	ipv6 nd prefix default no-autoconfig
	no shutdown
	standby version 2
	standby 40 ipv6 autoconfig
	standby 40 priority 100
	exit

username admin password admin
ip domain-name itsoeh.edu
crypto key generate rsa
    1024
line vty 0 15
	transport input ssh
	login local
	exit
```

---
### Router R4

```bash
enable
configure terminal
line console 0
	logging synchronous
	exit
	
hostname R4
enable password cisco
enable secret tics

interface g 0/1
	no shutdown
	exit

ipv6 unicast-routing

ipv6 dhcp pool DHCP-STATEFUL-10
	address prefix 2001:db8:3c4d:10::/64
	domain-name tics.edu.mx
	exit
	
ipv6 dhcp pool DHCP-STATEFUL-20
	address prefix 2001:db8:3c4d:20::/64
	domain-name tics.edu.mx
	exit
	
ipv6 dhcp pool DHCP-STATEFUL-30
	address prefix 2001:db8:3c4d:30::/64
	domain-name tics.edu.mx
	exit
	
ipv6 dhcp pool DHCP-STATEFUL-40
	address prefix 2001:db8:3c4d:40::/64
	domain-name tics.edu.mx
exit

interface g 0/1.10
	encapsulation dot1Q 10
	no ip address
	ipv6 address 2001:db8:3c4d:10::/64 eui-64
	ipv6 enable
	ipv6 nd managed-config-flag
	ipv6 nd prefix default no-autoconfig
	ipv6 dhcp server DHCP-STATEFUL-10
	no shutdown
	standby version 2
	standby 10 ipv6 autoconfig
	standby 10 priority 150
	standby 10 preempt
	exit
	
interface g 0/1.20
	encapsulation dot1Q 20
	no ip address
	ipv6 address 2001:db8:3c4d:20::/64 eui-64
	ipv6 enable
	ipv6 nd managed-config-flag
	ipv6 nd prefix default no-autoconfig
	ipv6 dhcp server DHCP-STATEFUL-20
	no shutdown
	standby version 2
	standby 20 ipv6 autoconfig
	standby 20 priority 150
	standby 20 preempt
	exit
	
interface g 0/1.30
	encapsulation dot1Q 30
	no ip address
	ipv6 address 2001:db8:3c4d:30::/64 eui-64
	ipv6 enable
	ipv6 nd managed-config-flag
	ipv6 nd prefix default no-autoconfig
	ipv6 dhcp server DHCP-STATEFUL-30
	no shutdown
	standby version 2
	standby 30 ipv6 autoconfig
	standby 30 priority 150
	standby 30 preempt
	exit
	
interface g 0/1.40
	encapsulation dot1Q 40 native
	no ip address
	ipv6 address 2001:db8:3c4d:40::/64 eui-64
	ipv6 enable
	ipv6 nd managed-config-flag
	ipv6 nd prefix default no-autoconfig
	ipv6 dhcp server DHCP-STATEFUL-40
	no shutdown
	standby version 2
	standby 40 ipv6 autoconfig
	standby 40 priority 150
	standby 40 preempt
	exit

username admin password admin
ip domain-name itsoeh.edu
crypto key generate rsa
    1024
line vty 0 15
	transport input ssh
	login local
	exit
```

---

## Dispositivos en progreso

* RA
* RB
* Antenas 1 y 2

---

## Verificaciones

* Pruebas de conectividad IPv6 entre VLANs.
* Validación de asignación DHCPv6 (stateless/stateful).
* Verificación de seguridad en puertos.
* Comprobación de enlaces EtherChannel.

| Propósito (Qué quieres saber) | Dispositivo | Comando |
| :--- | :--- | :--- |
| **Ver la IP del cliente (DHCP/SLAAC)** | PC | `ipconfig` |
| **Ver estado de Redundancia (Activo/Standby)** | Router (R1, R2, R3, R4) | `show standby brief` |
| **Ver clientes DHCPv6 (Prueba de Stateful)** | Router (R1, R4) | `show ipv6 dhcp binding` |
| **Ver enlaces agregados (EtherChannel)** | Switch (Todos) | `show etherchannel summary` |
| **Ver puertos troncales (Trunks)** | Switch (Todos) | `show interfaces trunk` |
| **Ver estado de bucles (STP)** | Switch (Todos) | `show spanning-tree` |
| **Ver tabla de enrutamiento (Inter-VLAN)** | Router (Todos) | `show ipv6 route` |
| **Ver seguridad de puerto (Port Security)** | Switch (SA, S1) | `show port-security interface [ID]` |  

---

### Fin del documento

*Este README resume las configuraciones completas del proyecto integrador Legacy, organizadas por edificio y tipo de servicio (Stateless/Stateful).*

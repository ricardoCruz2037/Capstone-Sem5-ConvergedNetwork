# Redes — Network Design and Implementation

Dentro de este módulo se documentan el diseño, configuración e implementación de la **red convergente** que conecta las dos sedes del proyecto a través de un **enlace inalámbrico punto a punto**.

## Objetivos
- Diseñar una red convergente que integre VLANs, ACLs y DHCP.
- Implementar enlaces punto a punto entre edificios.
- Configurar enrutamiento dinámico (EIGRP/OSPF) para la simulación WAN.
- Garantizar segmentación y seguridad en la comunicación.

## Contenido
| Elemento | Descripción |
|-----------|--------------|
| `topology.pkt` | Simulación principal en Cisco Packet Tracer. |
| `configs/` | Archivos de configuración de routers y switches (.txt). |
| `images/` | Diagramas de topología y resultados de simulaciones. |
| `reporte-redes.md` | Documento técnico que describe direccionamiento, VLANs y protocolos. |

## Tecnologías Utilizadas
- Cisco Packet Tracer / GNS3  
- Protocolos: VLANs, ACLs, DHCP, EIGRP, OSPF  
- Equipos utilizados y simulados: Routers 2911, Switches 2960, Ubiquiti Powerbeam Pbe-5ac-iso-gen2  

## Competencias Aplicadas
- Diseño e implementación de topologías LAN/WAN.  
- Segmentación lógica mediante VLANs.  
- Configuración de políticas de acceso y seguridad.  
- Pruebas de conectividad y simulación de tráfico.

---
> *La red diseñada sirve como base para la comunicación segura y eficiente entre módulos de desarrollo y bases de datos del proyecto Capstone.*

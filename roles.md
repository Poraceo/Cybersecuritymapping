# MAPA DE CARRERAS EN CIBERSEGURIDAD — LATAM 2026

<!--
================================================================
ARCHIVO EDITABLE — INSTRUCCIONES BÁSICAS
================================================================
Este archivo controla TODO lo que aparece en los HTMLs.
Después de editar este archivo, corre en la terminal:
    python actualizar.py

Eso regenera todos los archivos:
  - Mapa_General_Carreras.html  (vista panorámica interactiva con filtros)
  - Mapa_Carreras_Ciberseguridad.html  (versión con navegación detallada)
  - Mapa_Mental_Carreras.html   (vista por niveles)
  - Mapa_General_Carreras.png   (imagen estática para compartir)

================================================================
QUÉ PUEDES EDITAR EN CADA ROL (todos los @ que ves):
================================================================
OBLIGATORIOS (no los borres, solo cambia su valor):
  @rolES         → Nombre del rol en español
  @cat           → Categoría (debe coincidir con las claves de abajo)
  @nivel         → Nivel (junior / mid / senior / manager / executive)
  @anos          → Rango de años de experiencia
  @sinonimos     → Otros nombres del rol (separados por · )
  @salario_mes   → Rango mensual en USD: "$X,XXX - $X,XXX"
  @salario_ano   → Rango anual en USD
  @demanda       → MUY ALTA / ALTA / MEDIA / EXPLOSIVA
  @remoto        → Tipo de trabajo (remoto, híbrido, etc.)
  @relacionados  → IDs de otros roles relacionados (números separados por coma)

OPCIONALES (puedes agregarlos a cualquier rol — aparecen como
"Proyecciones 2026-2028" en el detalle):
  @proyeccion       → Crecimiento esperado (ej: "+45% en 3 años")
  @tendencia        → Tendencia 2026-2028 (texto libre)
  @salto_salarial   → De cuánto a cuánto crece el sueldo Junior→Senior
  @dificultad       → Dificultad de entrada (Baja/Media/Alta/Muy alta)

================================================================
SECCIONES (las que empiezan con ###) son listas o párrafos:
  ### Descripción      → Texto largo, qué hace el rol
  ### Hard Skills      → Lista con "-" cada uno
  ### Tools            → Lista con "-" cada uno
  ### Soft Skills      → Lista con "-" cada uno
  ### Certs            → Lista con "-" cada uno
  ### Cómo empezar     → Texto, cómo entrar al rol
  ### Crecimiento      → Texto, camino de carrera
  ### Mercados         → Texto, países y empresas que contratan
================================================================

REGLAS DE EDICIÓN:
- No borres las líneas con @ obligatorias (son campos que el script lee).
- Sí puedes editar el valor de cada @campo libremente.
- Las claves de las categorías (defensive, offensive, etc.) NO se cambian;
  solo el nombre visible y el color.
- Para AGREGAR un rol nuevo: copia un bloque "## Rol #XX" completo y dale
  un ID nuevo (51, 52, etc.). Mantén el orden numérico.
- Para BORRAR un rol: borra todo su bloque entre "## Rol #XX" y el siguiente.
- Si borras un rol, quita su número de los @relacionados de otros roles.
================================================================
-->

## CONFIGURACIÓN GLOBAL

@titulo: Mapa de Carreras en Ciberseguridad
@subtitulo: 50 ROLES · AMÉRICA 2026
@stat_salario_max: $470K
@stat_crecimiento: +29%

---

## CATEGORÍAS

<!-- Formato: @categoria CLAVE: Nombre visible | #COLOR-HEX
     Las claves (defensive, offensive, etc.) NO las cambies; solo el nombre y color.
-->
@categoria defensive: Defensivo / Blue Team | #60A5FA
@categoria offensive: Ofensivo / Red Team | #F87171
@categoria architecture: Arquitectura / Ingeniería | #34D399
@categoria specialized: Especializado | #C084FC
@categoria grc: GRC / Cumplimiento | #FBBF24
@categoria legal: Legal / Privacidad | #FB923C
@categoria leadership: Gerencial / Liderazgo | #F472B6
@categoria sales: Ventas / Consultoría | #818CF8
@categoria awareness: Awareness / Educación | #22D3EE
@categoria operations: Operaciones | #9CA3AF
@categoria ecosystem: Soporte al Ecosistema | #D4D4D8

---

## NIVELES

<!-- Formato: @nivel CLAVE: Nombre | Rango años | Descripción corta -->
@nivel junior: Junior | 0-3 años | Punto de entrada, sin o poca experiencia
@nivel mid: Mid-Level | 3-7 años | Profesional con experiencia sólida
@nivel senior: Senior | 5-12 años | Experto técnico independiente
@nivel manager: Manager / Lead | 7-12 años | Líder de equipo o programa
@nivel executive: Director / C-Level | 10+ años | Liderazgo ejecutivo

---

## ROLES TRENDING 2026

<!-- Los IDs de los roles "más calientes" que aparecen en la sección Emergentes -->
@trending: 23, 13, 25, 19, 15, 14, 12, 38, 32, 9

---

# LOS 50 ROLES

<!-- ============================================================ -->
<!-- Cada rol empieza con "## Rol #XX: Nombre"                    -->
<!-- ============================================================ -->

## Rol #01: SOC Analyst Tier 1
@rolES: Analista SOC Nivel 1
@cat: defensive
@nivel: junior
@anos: 0-2 años
@sinonimos: Security Operations Analyst · Junior SecOps
@salario_mes: $700 - $6,700
@salario_ano: $8,400 - $80,000
@demanda: MUY ALTA
@remoto: Híbrido (turnos 24/7)
@relacionados: 2, 3, 4, 38
@proyeccion: +18% en 2 años (entry-level más demandado en LATAM)
@tendencia: AI augmenting alert triage pero NO reemplazando analistas. MSSPs duplicando equipos.
@salto_salarial: De $8K (Junior LATAM) a $80K (Senior USA) — camino comprobado
@dificultad: Baja (con Security+ y ganas, 6 meses de prep)

### Descripción
Monitorea dashboards SIEM 24/7. Hace triage de 50-150 alertas diarias, descarta falsos positivos, sigue runbooks y escala incidentes a Tier 2. Es el punto de entrada masivo en ciberseguridad.

### Hard Skills
- TCP/IP y redes
- Windows/Linux básico
- Active Directory
- MITRE ATT&CK básico
- Logs y eventos
- Scripting básico

### Tools
- Splunk
- Microsoft Sentinel
- QRadar
- Chronicle
- CrowdStrike
- SentinelOne
- Defender

### Soft Skills
- Atención al detalle
- Tolerancia a turnos 24/7
- Comunicación escrita
- Manejo de estrés
- Trabajo en equipo

### Certs
- CompTIA Security+ ⭐
- Microsoft SC-200
- BTL1
- ISC2 CC
- Splunk Core

### Cómo empezar
Saca Security+, haz TryHackMe SOC Level 1, monta home lab con Splunk Free, aplica a MSSPs o bancos.

### Crecimiento
SOC Tier 2 → Tier 3 / Threat Hunter → Detection Engineer → Incident Responder

### Mercados
USA, Canadá, México, Brasil, Chile, Colombia. MSSPs grandes: Cipher, IQSEC, A3Sec, ETEK, NeoSecure, ISH, Tempest

---

## Rol #02: SOC Analyst Tier 2
@rolES: Analista SOC Nivel 2
@cat: defensive
@nivel: mid
@anos: 2-5 años
@sinonimos: Mid SecOps Analyst
@salario_mes: $1,200 - $10,800
@salario_ano: $14,000 - $130,000
@demanda: ALTA
@remoto: Híbrido y remoto creciente
@relacionados: 1, 3, 4, 6

### Descripción
Investiga incidentes escalados desde Tier 1, hace forensics ligero, autoriza contención, correlaciona eventos complejos, mejora detecciones y mentorea a Tier 1.

### Hard Skills
- Análisis profundo de logs
- Network forensics básico
- Malware triage
- KQL/SPL intermedio
- MITRE ATT&CK profundo
- Python/PowerShell

### Tools
- SIEMs avanzados
- EDRs (CrowdStrike, SentinelOne)
- Wireshark
- Volatility
- Any.Run
- TheHive

### Soft Skills
- Pensamiento crítico
- Capacidad analítica
- Comunicación a stakeholders
- Mentoría
- Gestión de prioridades

### Certs
- CompTIA CySA+ ⭐
- GCIH
- ECIH
- BTL2
- Microsoft SC-200

### Cómo empezar
Promoción interna desde Tier 1. Certifica CySA+/GCIH y domina un SIEM a nivel ingeniería.

### Crecimiento
SOC Tier 3 → Threat Hunter / Detection Engineer / IR Senior

### Mercados
USA, Canadá, México, Brasil. Bancos, fintechs (Nubank, Mercado Libre, Bitso), MSSPs internacionales

---

## Rol #03: SOC Analyst Tier 3 / Threat Hunter
@rolES: Cazador de Amenazas
@cat: defensive
@nivel: senior
@anos: 5-8 años
@sinonimos: Senior SOC Analyst · Threat Hunter
@salario_mes: $3,000 - $18,300
@salario_ano: $36,000 - $220,000
@demanda: MUY ALTA
@remoto: Remoto disponible (mayoría)
@relacionados: 2, 4, 6, 9

### Descripción
Threat hunting proactivo basado en hipótesis y TTPs, escribe reglas Sigma/YARA, desarrolla detecciones custom, lidera investigaciones complejas y define la estrategia de detección del SOC.

### Hard Skills
- KQL/SPL/EQL avanzado
- MITRE ATT&CK profundo
- Threat modeling
- Análisis adversario
- Python avanzado
- Data analysis

### Tools
- Sigma
- YARA
- ELK
- Splunk avanzado
- Sentinel
- Velociraptor
- Jupyter
- MISP

### Soft Skills
- Pensamiento crítico avanzado
- Hipótesis científica
- Comunicación ejecutiva
- Mentoría
- Autoaprendizaje
- Storytelling

### Certs
- GCFA
- GCIA
- GNFA
- OSCP
- CISSP
- GCTI

### Cómo empezar
Avanza desde Tier 2 con certs GCFA/GCIA + crea blog de threat hunting + contribuye a Sigma/Atomic Red Team.

### Crecimiento
Detection Engineering Lead → SOC Manager → Security Architect defensivo

### Mercados
USA principalmente. En LATAM: bancos top, fintechs, MSSPs grandes (Tempest, ISH, Cipher, IQSEC)

---

## Rol #04: Incident Responder / DFIR Analyst
@rolES: Respondedor a Incidentes / Forense Digital
@cat: defensive
@nivel: mid
@anos: 3-7 años
@sinonimos: DFIR Analyst · IR Engineer
@salario_mes: $2,300 - $17,900
@salario_ano: $28,000 - $215,000
@demanda: MUY ALTA
@remoto: Remoto + viajes ocasionales
@relacionados: 3, 5, 6, 32

### Descripción
Activa playbooks ante brechas, ejecuta cadena de custodia legal, hace análisis de memoria/disco/red, redacta reportes para legal y ejecutivos, coordina con comunicaciones en crisis.

### Hard Skills
- Forensics Windows/Linux/Mac
- Análisis de memoria (Volatility)
- Timeline analysis
- Network forensics
- Chain of custody
- Malware triage

### Tools
- EnCase
- FTK
- Autopsy
- SIFT
- Volatility
- Velociraptor
- KAPE
- X-Ways
- Magnet AXIOM

### Soft Skills
- Calma bajo presión extrema
- Comunicación con ejecutivos/legal
- Redacción técnico-legal
- Ética inquebrantable
- Gestión en crisis

### Certs
- GCFA ⭐ (gold standard)
- GCIH
- GNFA
- GREM
- EnCE

### Cómo empezar
Sal de SOC Tier 2/3 con GCFA + participa en CTFs DFIR + blog de casos reales (anonimizados).

### Crecimiento
Senior DFIR → DFIR Lead → Director of IR → Field CISO

### Mercados
USA, Canadá, Brasil, México. Big4 (Deloitte, KPMG, EY, PwC), Mandiant, CrowdStrike Services, MSSPs

---

## Rol #05: Malware Analyst / Reverse Engineer
@rolES: Analista de Malware / Ingeniero Inverso
@cat: defensive
@nivel: senior
@anos: 4-8 años
@sinonimos: Reverse Engineer · Threat Researcher
@salario_mes: $2,800 - $24,800
@salario_ano: $33,000 - $297,000
@demanda: MEDIA-ALTA (perfil escaso)
@remoto: Remoto total (la mayoría)
@relacionados: 4, 6, 50

### Descripción
Análisis estático y dinámico de malware, ingeniería inversa de binarios, extrae IOCs y TTPs, escribe firmas YARA, descompila para entender funcionalidad, publica research técnico.

### Hard Skills
- Assembly (x86/x64/ARM)
- C/C++
- Python
- Debugging avanzado
- SO a bajo nivel
- Anti-debugging

### Tools
- IDA Pro
- Ghidra
- x64dbg
- OllyDbg
- Cuckoo Sandbox
- REMnux
- FLARE-VM
- radare2

### Soft Skills
- Paciencia extrema
- Persistencia
- Atención obsesiva al detalle
- Autoaprendizaje
- Escritura técnica avanzada

### Certs
- GREM ⭐ (gold standard)
- OSCE3
- OSEE
- CARP

### Cómo empezar
Domina assembly + crackmes.one + blog de análisis + contribuir a malware repositories.

### Crecimiento
Senior RE → Principal Researcher → Threat Research Lead

### Mercados
USA. Vendors: Mandiant, Unit 42, Talos, CrowdStrike, Kaspersky GReAT, ESET LATAM (Argentina)

---

## Rol #06: Threat Intelligence Analyst (CTI)
@rolES: Analista de Inteligencia de Amenazas
@cat: defensive
@nivel: mid
@anos: 3-7 años
@sinonimos: CTI Analyst · OSINT Analyst
@salario_mes: $1,700 - $13,300
@salario_ano: $20,000 - $160,000
@demanda: ALTA
@remoto: Remoto disponible
@relacionados: 3, 5, 50

### Descripción
Recolecta y analiza IOCs, monitorea dark web y foros, perfila actores de amenaza (APTs), mapea TTPs a MITRE ATT&CK y Diamond Model, produce informes para ejecutivos.

### Hard Skills
- OSINT
- Análisis estructurado (ACH, SATs)
- MITRE ATT&CK
- Diamond/Kill Chain
- Geopolítica cibernética

### Tools
- MISP
- TheHive
- Recorded Future
- ThreatConnect
- Maltego
- Shodan
- VirusTotal
- AlienVault OTX

### Soft Skills
- Pensamiento crítico
- Escritura analítica y ejecutiva
- Presentación a C-level
- Escepticismo
- Ética en investigación

### Certs
- CTIA (EC-Council)
- GCTI ⭐
- CySA+
- MAD20 ATT&CK Defender

### Cómo empezar
Background en periodismo/inteligencia ayuda. Empieza con OSINT en TraceLabs + blog de research.

### Crecimiento
Senior CTI Analyst → CTI Lead → Head of Threat Intelligence

### Mercados
USA, Brasil. Vendors (Mandiant, Recorded Future, Flashpoint), bancos grandes, gobierno, MSSPs

---

## Rol #07: Junior Penetration Tester
@rolES: Pentester Junior / Hacker Ético
@cat: offensive
@nivel: junior
@anos: 0-2 años
@sinonimos: Ethical Hacker Junior
@salario_mes: $700 - $8,300
@salario_ano: $8,400 - $100,000
@demanda: ALTA (mercado competido)
@remoto: Remoto frecuente
@relacionados: 8, 10, 12

### Descripción
Ejecuta pruebas de penetración web/red/cloud bajo supervisión, sigue metodologías (OWASP, PTES), escribe reportes técnicos y ejecutivos, participa en internal pentests.

### Hard Skills
- OWASP Top 10
- Redes fundamentales
- Linux/Windows
- Active Directory básico
- Python/Bash
- HTTP/HTTPS
- SQL básico

### Tools
- Burp Suite
- Nmap
- Metasploit
- Kali Linux
- Nuclei
- ffuf
- sqlmap
- Hashcat
- BloodHound

### Soft Skills
- Persistencia
- Pensamiento creativo
- Ética profesional
- Escritura clara
- Comunicación con clientes

### Certs
- eJPT (entry)
- CPTS (HackTheBox) ⭐
- PNPT (TCM)
- PenTest+

### Cómo empezar
Saca eJPT/CPTS/PNPT + completa HTB/THM + build portfolio con writeups + bug bounty inicial.

### Crecimiento
Pentester → Senior Pentester → Red Team Operator → Red Team Lead

### Mercados
USA, México, Brasil, Argentina, Chile, Colombia. Boutiques: Tempest, HackerSec, DeepStrike, IQSEC, A3Sec

---

## Rol #08: Senior Pentester / Red Team Operator
@rolES: Pentester Senior / Operador Red Team
@cat: offensive
@nivel: senior
@anos: 4-8 años
@sinonimos: Red Team Operator
@salario_mes: $2,800 - $16,700
@salario_ano: $33,000 - $200,000
@demanda: MUY ALTA en LATAM banca/fintech
@remoto: Remoto disponible
@relacionados: 7, 9, 10

### Descripción
Lidera engagements ofensivos avanzados, simula APTs, ejecuta operaciones de Red Team con sigilo, bypass de EDR/AV, ataques avanzados a AD, mentorea juniors.

### Hard Skills
- AD avanzado (Kerberoasting, ADCS)
- Evasión EDR/AV
- Ataques cloud (Azure AD/AWS/GCP)
- C2 frameworks
- Malware dev básico

### Tools
- Cobalt Strike
- Sliver
- Mythic
- Havoc
- BloodHound
- Rubeus
- Mimikatz
- Brute Ratel

### Soft Skills
- Liderazgo de engagements
- Escritura ejecutiva
- Presentación a CISOs
- Ética estricta
- Creatividad bajo restricciones

### Certs
- OSCP ⭐ (baseline)
- OSEP
- OSWE
- CRTO
- CRTP
- OSCE3

### Cómo empezar
Avanza desde Junior Pentester con OSCP + portfolio público (CVEs, conferencias, blog).

### Crecimiento
Red Team Lead → Offensive Security Manager → Director of Offensive Security

### Mercados
USA, Canadá, México, Brasil, Argentina, Chile. Boutiques ofensivas, banca top, Big4, Mandiant Red Team

---

## Rol #09: Red Team Lead
@rolES: Líder de Red Team / Emulador de Adversarios
@cat: offensive
@nivel: manager
@anos: 7+ años
@sinonimos: Adversary Emulation Specialist
@salario_mes: $5,800 - $20,800
@salario_ano: $70,000 - $250,000
@demanda: ALTA (perfil escaso)
@remoto: Remoto
@relacionados: 8, 3, 38

### Descripción
Diseña operaciones de Red Team de largo alcance, emula APTs basados en CTI, gestiona equipo de operadores, define scope con CISOs, lidera ejercicios purple team.

### Hard Skills
- Threat-informed defense
- Adversary emulation
- TIBER-EU framework
- MITRE ATT&CK Evaluations
- Custom malware design
- OPSEC

### Tools
- MITRE CALDERA
- Atomic Red Team
- Cobalt Strike maestro
- Prelude Operator
- Vectr

### Soft Skills
- Liderazgo estratégico
- Gestión de equipo
- Comunicación ejecutiva
- Gestión de presupuesto
- Negociación con clientes

### Certs
- OSCE3
- CRTL ⭐
- GIAC Red Team Pro
- CISSP

### Cómo empezar
Avanza desde Senior Pentester con años de operaciones + reputación pública.

### Crecimiento
Director of Offensive Security → CISO con perfil ofensivo

### Mercados
USA principalmente. En LATAM: bancos top, consultoras grandes, Mandiant LATAM, IBM X-Force

---

## Rol #10: Bug Bounty Hunter
@rolES: Cazador de Bugs / Investigador
@cat: offensive
@nivel: mid
@anos: Variable (skills > años)
@sinonimos: Security Researcher independiente
@salario_mes: $0 - $40,000+ (variable)
@salario_ano: $0 - $500,000+ (variable)
@demanda: ALTA (primary o complementario)
@remoto: 100% remoto / independiente
@relacionados: 7, 8, 5

### Descripción
Identifica vulnerabilidades en plataformas (HackerOne, Bugcrowd, Intigriti), escribe reportes técnicos, busca 0-days, publica research, participa en pwn2own.

### Hard Skills
- OWASP Top 10 profundo
- Lógica de negocio
- IDOR/SSRF/Prototype pollution
- Race conditions
- Cloud-specific bugs
- Exploit dev

### Tools
- Burp Suite Pro
- Caido
- Custom scripts
- Frida
- IDA
- Ghidra
- ZAP
- ffuf
- Nuclei

### Soft Skills
- Persistencia absoluta
- Autodisciplina
- Escritura técnica alta
- Manejo de rechazo
- Networking en comunidad
- Tolerancia a ingresos variables

### Certs
- OSCP
- OSWE
- Reputación en H1/Bugcrowd > certs

### Cómo empezar
Empieza en HackerOne con tutoriales, lee reportes públicos disclosed, participa en CTFs ofensivos.

### Crecimiento
Top researcher → Pwn2Own → Founder de boutique → CTO/Researcher

### Mercados
Global. Top hunters latinos compiten globalmente; programas USA pagan más

---

## Rol #11: Security Engineer
@rolES: Ingeniero de Seguridad
@cat: architecture
@nivel: mid
@anos: 3-6 años
@sinonimos: Cybersecurity Engineer
@salario_mes: $1,200 - $13,300
@salario_ano: $14,000 - $160,000
@demanda: MUY ALTA (rol troncal)
@remoto: Híbrido y remoto
@relacionados: 12, 13, 14, 16

### Descripción
Diseña, implementa y mantiene controles de seguridad: firewalls, WAFs, IPS/IDS, SIEM, EDR, VPN, MFA. Endurece configuraciones, automatiza despliegues, soporta operaciones.

### Hard Skills
- Networking (TCP/IP, BGP)
- Linux/Windows hardening
- IAM
- Criptografía aplicada
- Ansible/Terraform
- Python/Bash/PowerShell

### Tools
- Palo Alto
- Fortinet
- Check Point
- Cisco ASA
- F5
- Splunk
- Sentinel
- CrowdStrike
- Tenable

### Soft Skills
- Resolución de problemas
- Gestión de proyectos
- Documentación
- Comunicación con IT y dev
- Ownership

### Certs
- Security+
- CCNP Security
- CCSP
- CISSP
- AWS Security
- AZ-500

### Cómo empezar
Desde Sysadmin/Network + Security+ + experiencia con un firewall enterprise.

### Crecimiento
Senior Security Engineer → Security Architect → Principal Engineer

### Mercados
USA, Canadá, México, Brasil, Chile, Colombia, Argentina. Bancos, telcos, fintechs, enterprise

---

## Rol #12: Application Security (AppSec) Engineer
@rolES: Ingeniero de Seguridad de Aplicaciones
@cat: architecture
@nivel: mid
@anos: 4-8 años
@sinonimos: Product Security Engineer
@salario_mes: $3,000 - $17,500
@salario_ano: $36,000 - $210,000
@demanda: MUY ALTA (escasez global)
@remoto: Remoto disponible
@relacionados: 11, 13, 14, 23

### Descripción
Ejecuta threat modeling (STRIDE/PASTA), code reviews de seguridad, integra SAST/DAST/SCA en pipelines, mentorea developers en secure coding, lidera secure SDLC.

### Hard Skills
- OWASP Top 10 profundo
- Code review (Java, Python, Go, JS)
- Threat modeling
- Criptografía
- Supply chain security
- SBOM

### Tools
- Burp Pro
- Semgrep
- Snyk
- Checkmarx
- Veracode
- SonarQube
- OWASP ZAP
- Trivy

### Soft Skills
- Pedagogía con devs
- Comunicación cross-team
- Paciencia
- Balance security vs velocity
- Mentoría
- Negociación

### Certs
- CSSLP ⭐
- OSWE
- GWAPT
- CISSP
- eWPTX

### Cómo empezar
Desde Software Developer con interés en seguridad + CSSLP + Portswigger Web Security Academy.

### Crecimiento
AppSec Lead → Security Architect → Principal AppSec

### Mercados
USA, México, Brasil, Argentina, Chile. Big Tech, fintechs, scaleups, banca digital (Nubank, Bitso, Mercado Libre)

---

## Rol #13: DevSecOps Engineer
@rolES: Ingeniero DevSecOps
@cat: architecture
@nivel: mid
@anos: 4-8 años
@sinonimos: Platform Security Engineer
@salario_mes: $3,300 - $17,500
@salario_ano: $40,000 - $210,000
@demanda: MUY ALTA (más caliente 2025-2026)
@remoto: Remoto total muy común
@relacionados: 12, 14, 25
@proyeccion: +45% en demanda esperado para 2027
@tendencia: Shift-left + supply chain security son OBLIGATORIOS en cualquier empresa cloud-native
@salto_salarial: De $40K (Junior LATAM) a $210K (Senior USA) — 5x de crecimiento
@dificultad: Media (más fácil con base de DevOps previa)

### Descripción
Integra seguridad en CI/CD pipelines, implementa policy-as-code, gestiona secretos, asegura supply chain (Sigstore, SBOM), automatiza compliance, shift-left security.

### Hard Skills
- CI/CD pipelines
- Kubernetes
- Docker
- IaC (Terraform)
- Policy-as-code (OPA)
- Secrets management
- Container security

### Tools
- Terraform
- Kubernetes
- Docker
- GitHub Actions
- ArgoCD
- Vault
- Falco
- Trivy
- Cosign/Sigstore

### Soft Skills
- Mentalidad de automatización
- Pragmatismo
- Comunicación con devs y ops
- Ownership
- Mejora continua

### Certs
- CKS ⭐ (Kubernetes Security)
- AWS Security
- Practical DevSecOps CDP/CDE
- CISSP

### Cómo empezar
Desde DevOps Engineer + cursos de container/K8s security + Practical DevSecOps.

### Crecimiento
DevSecOps Lead → Cloud Security Architect → Principal Engineer

### Mercados
USA, Canadá, Brasil, México, Argentina, Chile. Toda empresa cloud-native, fintechs, SaaS, scaleups

---

## Rol #14: Cloud Security Engineer
@rolES: Ingeniero de Seguridad en la Nube
@cat: architecture
@nivel: mid
@anos: 3-7 años
@sinonimos: Cloud Security Specialist
@salario_mes: $3,300 - $14,600
@salario_ano: $40,000 - $175,000
@demanda: MUY ALTA (escasez crítica)
@remoto: Remoto total muy común
@relacionados: 13, 15, 17

### Descripción
Asegura entornos AWS/Azure/GCP, configura controles nativos (GuardDuty, Defender, SCC), implementa CSPM/CWPP/CNAPP, gestiona IAM cloud, asegura workloads serverless y containers.

### Hard Skills
- AWS/Azure/GCP profundo
- IAM cloud
- Networking cloud
- Kubernetes
- Serverless security
- IaC security

### Tools
- GuardDuty
- Security Hub
- Azure Defender
- GCP SCC
- Wiz
- Prisma Cloud
- Lacework
- Orca

### Soft Skills
- Curiosidad continua (cloud cambia)
- Automatización mentality
- Documentación
- Gestión de riesgo
- Pragmatismo

### Certs
- AWS Security Specialty ⭐
- Azure AZ-500
- GCP Pro Cloud Security
- CCSP
- CCSK

### Cómo empezar
Desde Cloud Engineer/DevOps + AWS Security Specialty + Wiz/Prisma hands-on.

### Crecimiento
Cloud Security Architect → Principal → CISO (track cloud)

### Mercados
USA, Canadá, Brasil, México, Argentina, Chile. Cualquier empresa con cloud (casi todas)

---

## Rol #15: Cloud Security Architect
@rolES: Arquitecto de Seguridad en la Nube
@cat: architecture
@nivel: senior
@anos: 7-12 años
@sinonimos: Senior Cloud Security Architect
@salario_mes: $5,800 - $24,200
@salario_ano: $70,000 - $290,000
@demanda: MUY ALTA (mejor pagado en cloud)
@remoto: Remoto total común
@relacionados: 14, 16, 19

### Descripción
Diseña arquitecturas de seguridad cloud enterprise, define landing zones seguras, modela amenazas arquitectónicamente, lidera migraciones cloud seguras, presenta a C-level.

### Hard Skills
- Arquitectura referencia AWS/Azure/GCP
- Zero Trust
- Well-Architected (security pillar)
- Multi-cloud
- Hybrid cloud
- Regulatory compliance

### Tools
- Wiz
- Prisma Cloud
- Lacework
- Orca
- Terraform avanzado
- AWS Organizations
- Azure Management Groups

### Soft Skills
- Pensamiento estratégico
- Comunicación ejecutiva
- Liderazgo técnico
- Mentoría
- Visión de negocio

### Certs
- CCSP ⭐
- CCSK
- AWS Solutions Architect Pro + Security
- Azure SC-100

### Cómo empezar
Avanza desde Cloud Security Engineer con experiencia en migraciones grandes + SC-100/AWS Pro.

### Crecimiento
Principal Architect → Distinguished Engineer → CISO

### Mercados
USA, Canadá, Brasil, México. Big Tech, enterprise migrations, consultoras estratégicas

---

## Rol #16: Security Architect
@rolES: Arquitecto de Seguridad
@cat: architecture
@nivel: senior
@anos: 8-15 años
@sinonimos: Enterprise Security Architect
@salario_mes: $5,800 - $20,800
@salario_ano: $70,000 - $250,000
@demanda: ALTA (estratégico necesario)
@remoto: Híbrido / Remoto
@relacionados: 11, 15, 19, 37

### Descripción
Define la arquitectura de seguridad enterprise-wide, alinea controles con business goals, modela amenazas a nivel sistémico, gobierna estándares, asesora al CISO.

### Hard Skills
- SABSA, TOGAF, NIST CSF
- Zero Trust
- Threat modeling avanzado
- Criptografía aplicada
- IAM enterprise
- Integración de domains

### Tools
- Frameworks de modelado
- Visio/Lucidchart
- Suite completa de seguridad enterprise

### Soft Skills
- Pensamiento sistémico
- Comunicación con todos los niveles
- Negociación
- Liderazgo de influencia
- Visión de futuro

### Certs
- CISSP-ISSAP ⭐ (gold standard)
- SABSA SCF
- TOGAF
- CCSP

### Cómo empezar
Desde Senior Security Engineer + ISSAP/SABSA + experiencia liderando diseños.

### Crecimiento
Principal/Distinguished Architect → CISO

### Mercados
USA, México, Brasil. Bancos, seguros, gobierno, enterprise tech

---

## Rol #17: Network Security Engineer
@rolES: Ingeniero de Seguridad de Redes
@cat: architecture
@nivel: mid
@anos: 4-8 años
@sinonimos: Network Security Specialist
@salario_mes: $1,700 - $12,500
@salario_ano: $20,000 - $150,000
@demanda: ALTA (banca/telco LATAM)
@remoto: Híbrido típico
@relacionados: 11, 18, 19

### Descripción
Diseña y opera infraestructura de seguridad de red: firewalls NGFW, IPS/IDS, NAC, proxies, segmentación, DDoS protection, ZTNA. Crítico en banca LATAM.

### Hard Skills
- TCP/IP avanzado
- BGP
- Routing/switching
- VPN (IPSec, SSL)
- 802.1X, NAC
- Microsegmentación
- SD-WAN security
- ZTNA

### Tools
- Palo Alto NGFW
- Fortinet FortiGate
- Check Point
- Cisco ASA/Firepower/ISE
- F5 BIG-IP
- Zscaler
- Netskope

### Soft Skills
- Troubleshooting bajo presión
- Documentación de redes
- Comunicación con networking team
- Gestión de cambios

### Certs
- PCNSE (Palo Alto) ⭐
- Fortinet NSE 7/8
- CCNP Security
- Check Point CCSE
- Cisco CyberOps

### Cómo empezar
Desde Network Engineer + PCNSE/Fortinet NSE.

### Crecimiento
Senior Network Sec → Network Security Architect → Security Architect general

### Mercados
México, Brasil, Colombia, Chile, Argentina (bancos y telcos). USA en transición a cloud

---

## Rol #18: IAM / Identity Engineer
@rolES: Ingeniero de Identidad y Accesos
@cat: architecture
@nivel: mid
@anos: 3-7 años
@sinonimos: Identity Engineer · PAM Engineer
@salario_mes: $1,700 - $11,700
@salario_ano: $20,000 - $140,000
@demanda: ALTA (boom Zero Trust)
@remoto: Remoto disponible
@relacionados: 11, 19, 46

### Descripción
Implementa y opera SSO, MFA, lifecycle management de identidades, PAM (Privileged Access), federación, just-in-time access, governance de identidades.

### Hard Skills
- OAuth 2.0, OIDC, SAML, SCIM
- LDAP, AD profundo
- Zero Trust identity
- RBAC/ABAC
- Privileged Access Management

### Tools
- Okta
- Microsoft Entra ID
- SailPoint
- CyberArk
- BeyondTrust
- Ping Identity
- ForgeRock
- HashiCorp Vault

### Soft Skills
- Atención meticulosa
- Comunicación con HR/IT
- Documentación
- Paciencia con procesos complejos
- Ownership

### Certs
- Okta Certified Pro
- SailPoint IdentityNow
- CyberArk Defender/Sentry
- AZ-500

### Cómo empezar
Desde Sysadmin con AD + cert de Okta/Entra ID + experiencia en lifecycle.

### Crecimiento
Senior IAM Engineer → IAM Architect → Identity Director

### Mercados
USA, México, Brasil. Bancos, healthcare, enterprise grandes

---

## Rol #19: Zero Trust Architect
@rolES: Arquitecto de Confianza Cero
@cat: architecture
@nivel: senior
@anos: 8-12 años
@sinonimos: ZT Architect · SASE Architect
@salario_mes: $5,000 - $23,300
@salario_ano: $60,000 - $280,000
@demanda: MUY ALTA (emergente top 2025-2026)
@remoto: Remoto total común
@relacionados: 15, 16, 17, 18

### Descripción
Diseña la transformación Zero Trust en la empresa: identidad como perímetro, microsegmentación, ZTNA, conditional access, CNAPP, SASE. Rol emergente muy caliente.

### Hard Skills
- NIST 800-207
- CISA ZT Maturity
- SASE
- Microsegmentación
- ZTNA
- IAM avanzado
- BeyondCorp model

### Tools
- Zscaler
- Netskope
- Cloudflare Zero Trust
- Prisma Access
- Entra/Zero Trust suite
- Duo
- Illumio

### Soft Skills
- Visión estratégica
- Change management
- Comunicación con C-level
- Pedagogía organizacional
- Transformación cultural

### Certs
- SC-100 (Microsoft Cybersec Arch) ⭐
- CCSP
- CISSP-ISSAP
- Zscaler ZDX Pro

### Cómo empezar
Desde Security Architect/Network Arch + experiencia liderando una migración ZT real.

### Crecimiento
Principal Architect → CISO (track moderno)

### Mercados
USA, Canadá. En LATAM: enterprise top, banca, gobierno

---

## Rol #20: OT/ICS Security Engineer
@rolES: Ingeniero de Seguridad Industrial
@cat: specialized
@nivel: senior
@anos: 5-10 años (mix IT+OT)
@sinonimos: SCADA Security Engineer
@salario_mes: $3,800 - $13,300
@salario_ano: $45,000 - $160,000
@demanda: MUY ALTA en LATAM (energía/minería)
@remoto: Híbrido (visitas a plantas)
@relacionados: 11, 17, 21

### Descripción
Protege PLCs, SCADA, DCS, RTUs, HMIs en infraestructuras críticas (energía, agua, petróleo, manufactura, minería). Aplica modelo Purdue, IEC 62443, NIST SP 800-82.

### Hard Skills
- Protocolos industriales (Modbus, DNP3, OPC UA)
- Modelo Purdue
- ICS/SCADA architecture
- IEC 62443
- NERC CIP
- Ingeniería de procesos básica

### Tools
- Claroty
- Nozomi Networks
- Dragos
- Tenable.ot
- Forescout SilentDefense
- Industrial Defender

### Soft Skills
- Paciencia (cambios OT son lentos)
- Comunicación con ingenieros de planta
- Respeto por safety (vidas en juego)
- Seguridad física awareness

### Certs
- GICSP ⭐ (gold standard)
- GRID
- ISA/IEC 62443 Expert
- CSSA
- GCIP

### Cómo empezar
Desde Process Engineer/Network Engineer en industria + ISA 62443 Fundamentals → GICSP.

### Crecimiento
Senior OT → OT Security Architect → ICS Security Manager → CISO industria

### Mercados
Chile (minería), Perú (minería), Colombia (petróleo), México (petróleo, manufactura), Brasil, Argentina (energía)

---

## Rol #21: IoT/Embedded Security Engineer
@rolES: Ingeniero de Seguridad IoT
@cat: specialized
@nivel: senior
@anos: 5-9 años
@sinonimos: Embedded Security Researcher
@salario_mes: $3,800 - $14,200
@salario_ano: $45,000 - $170,000
@demanda: MEDIA-ALTA (nicho especializado)
@remoto: Híbrido (necesitas hardware)
@relacionados: 5, 20, 23

### Descripción
Hardware hacking, análisis de firmware, audita dispositivos IoT (médicos, automotive, smart home), analiza protocolos wireless, ataca/defiende dispositivos embebidos.

### Hard Skills
- C/C++/Rust embedded
- RTOS
- ARM/MIPS/AVR
- JTAG/SWD, UART, SPI, I2C
- Bluetooth/Zigbee/LoRa security
- Side-channel attacks

### Tools
- Ghidra
- IDA Pro
- JTAGulator
- Bus Pirate
- Saleae Logic
- Flipper Zero
- HackRF
- Proxmark
- ChipWhisperer

### Soft Skills
- Persistencia hardcore
- Paciencia para hardware tinkering
- Manejo manual
- Curiosidad técnica profunda
- Ética en research

### Certs
- OSED (Exploit Dev)
- GMOB
- PenTest+
- Reputación pública en research

### Cómo empezar
Desde Electrical Engineer/Firmware Developer + crackmes hardware + DEF CON Hardware Hacking Village.

### Crecimiento
Senior IoT Sec → IoT Security Architect → CTO en vendor IoT

### Mercados
USA principalmente, Brasil, México. Vendors IoT, automotive (Tesla, BMW), medical devices

---

## Rol #22: Mobile Security Engineer
@rolES: Ingeniero de Seguridad Móvil
@cat: specialized
@nivel: mid
@anos: 4-8 años
@sinonimos: Mobile AppSec Engineer
@salario_mes: $3,300 - $13,800
@salario_ano: $40,000 - $165,000
@demanda: ALTA en banca/fintech LATAM
@remoto: Remoto disponible
@relacionados: 7, 12, 23

### Descripción
Audita apps iOS/Android, dynamic instrumentation, identifica vulnerabilidades OWASP MASVS, asegura SDKs móviles, ataca/defiende apps bancarias/fintech.

### Hard Skills
- iOS/Android internals
- Objective-C/Swift
- Java/Kotlin
- Frida scripting
- MASVS/MASTG
- Certificate pinning
- Secure storage

### Tools
- Frida
- Objection
- MobSF
- Burp Suite + mobile
- Magisk
- Corellium
- Apktool
- JADX
- Hopper

### Soft Skills
- Paciencia con tooling
- Atención al detalle
- Escritura de reportes técnicos
- Comunicación con devs móviles

### Certs
- GMOB
- eMAPT
- OSWE (web relevante)
- Practical Mobile App Pentesting

### Cómo empezar
Desde Mobile Developer + Portswigger Mobile Academy + eMAPT.

### Crecimiento
Senior Mobile Sec → Mobile Security Lead → AppSec Architect

### Mercados
USA, Brasil, México. Fintechs (Nubank, Mercado Pago, Bitso, Clip), bancos digitales

---

## Rol #23: AI / ML Security Engineer
@rolES: Ingeniero de Seguridad de IA
@cat: specialized
@nivel: mid
@anos: 3-7 años
@sinonimos: MLSecOps Engineer · AI Red Teamer
@salario_mes: $4,200 - $24,200
@salario_ano: $50,000 - $290,000
@demanda: EXPLOSIVA (+24x demanda 2023-2026)
@remoto: Remoto total común
@relacionados: 10, 12, 31
@proyeccion: +200% en 3 años (rol más caliente del mercado)
@tendencia: Toda empresa con LLMs propios necesita uno. Gobierno y banca priorizando AI red teaming.
@salto_salarial: De $50K (Junior LATAM) a $290K (Senior USA) — el salto más alto del mercado
@dificultad: Alta (necesitas base de ML + seguridad)

### Descripción
Red teaming de LLMs (prompt injection, model extraction, poisoning), defensas MLSecOps, mapeo a MITRE ATLAS y OWASP Top 10 for LLM Applications, AI governance.

### Hard Skills
- ML/Deep Learning básico
- LLM security
- Prompt engineering
- Adversarial ML
- Model attacks
- RAG security

### Tools
- Microsoft PyRIT
- NVIDIA Garak
- HuggingFace
- AWS Bedrock security
- Robust Intelligence
- Lakera
- Protect AI
- MITRE ATLAS

### Soft Skills
- Curiosidad técnica acelerada
- Pensamiento adversarial
- Comunicación con data scientists
- Ethical reasoning

### Certs
- CAISP (Practical DevSecOps) ⭐
- AI Red Teamer (HackTheBox)
- AWS ML + Security Specialty
- ISO 42001 Lead Auditor

### Cómo empezar
Desde ML Engineer/Security Engineer + CAISP + portfolio público de AI red teaming.

### Crecimiento
AI Security Lead → AI Governance Director → Chief AI Security Officer

### Mercados
USA, Brasil emergente, México. Big Tech, AI labs, vendors (Robust Intelligence, Lakera, Protect AI)

---

## Rol #24: Cryptographer / Crypto Engineer
@rolES: Criptógrafo / Ingeniero Criptográfico
@cat: specialized
@nivel: senior
@anos: 5-12+ años (académico)
@sinonimos: Applied Cryptographer
@salario_mes: $5,800 - $20,800
@salario_ano: $70,000 - $250,000
@demanda: MEDIA (nicho extremadamente especializado)
@remoto: Remoto disponible
@relacionados: 12, 16, 18

### Descripción
Implementa criptografía a nivel de protocolo, gestiona HSMs, diseña PKI enterprise, migra a post-quantum crypto (Kyber, Dilithium), revisa implementaciones.

### Hard Skills
- Matemática discreta avanzada
- Álgebra abstracta
- Cripto aplicada (AES, RSA, ECC, lattice)
- PKI
- HSMs
- Post-quantum cryptography

### Tools
- Thales HSMs
- AWS KMS
- Azure Key Vault
- GCP KMS
- OpenSSL
- BouncyCastle
- libsodium
- Tamarin, ProVerif

### Soft Skills
- Rigor matemático
- Paciencia
- Escritura técnica precisa
- Comunicación con no criptógrafos

### Certs
- PhD frecuente (no obligatorio)
- CISSP
- EC-Council ECES

### Cómo empezar
Desde matemáticas/CS académico + investigación + portfolio académico. NO es entry-level path.

### Crecimiento
Senior Cryptographer → Distinguished Cryptographer / Crypto Architect

### Mercados
USA principalmente (defensa, fintech, blockchain), pocas posiciones en LATAM

---

## Rol #25: Kubernetes Security Specialist
@rolES: Especialista en Seguridad K8s
@cat: specialized
@nivel: mid
@anos: 3-6 años
@sinonimos: Container Security Engineer
@salario_mes: $3,800 - $16,700
@salario_ano: $45,000 - $200,000
@demanda: MUY ALTA (emergente y caliente)
@remoto: Remoto total
@relacionados: 13, 14, 15

### Descripción
Asegura clusters K8s, runtime protection (Falco, Tetragon), define network policies, gestiona admission controllers, escanea imágenes, hace IRT en K8s.

### Hard Skills
- Kubernetes profundo (RBAC, admission)
- Container runtime security
- eBPF basics
- Service mesh security (Istio, Linkerd)

### Tools
- Falco
- Tetragon
- Cilium
- Kyverno
- OPA Gatekeeper
- Trivy
- Sysdig Secure
- Aqua
- Istio mTLS

### Soft Skills
- Mentalidad de automatización
- Troubleshooting de sistemas distribuidos
- Comunicación con SREs/devs
- Ownership

### Certs
- CKS ⭐ (Certified Kubernetes Security)
- CKA prerequisite
- AWS Security Specialty

### Cómo empezar
Desde DevOps con K8s + CKA → CKS + lab con Falco/OPA.

### Crecimiento
Senior K8s Security → Platform Security Lead → Cloud Security Architect

### Mercados
USA, Brasil, México. SaaS, fintechs, cualquier empresa cloud-native moderna

---

## Rol #26: GRC Analyst Junior
@rolES: Analista GRC Junior
@cat: grc
@nivel: junior
@anos: 0-3 años
@sinonimos: Compliance Analyst · IT Risk Analyst
@salario_mes: $700 - $7,900
@salario_ano: $8,400 - $95,000
@demanda: ALTA (mejor camino no técnico)
@remoto: Híbrido / Remoto frecuente
@relacionados: 27, 28, 30, 31

### Descripción
Soporta auditorías SOC 2 / ISO 27001 / PCI-DSS / HIPAA, recolecta evidencia, mantiene registros de riesgos, redacta políticas, prepara documentación para auditores externos.

### Hard Skills
- NIST CSF, ISO 27001/27002
- COBIT, COSO ERM
- NIST RMF
- Redacción de políticas
- Gestión documental
- Controles de seguridad

### Tools
- ServiceNow GRC
- Archer
- LogicGate
- AuditBoard
- Vanta
- Drata
- Hyperproof
- OneTrust
- Excel avanzado

### Soft Skills
- Comunicación escrita excelente
- Atención al detalle
- Gestión de tiempo y deadlines
- Paciencia con burocracia
- Diplomacia interna

### Certs
- CompTIA Security+ ⭐
- ISC2 CC
- ISACA CGRC
- ISO 27001 Lead Implementer
- COBIT 2019 Foundation

### Cómo empezar
Desde QA / Audit / Legal / PM + Security+ + ISO 27001 LI.

### Crecimiento
Senior GRC → Compliance Officer → GRC Manager → CISO (no técnico)

### Mercados
USA, Canadá, México, Brasil, Colombia, Argentina. Bancos, seguros, healthcare, SaaS, todo lo regulado

---

## Rol #27: Senior GRC Analyst / Compliance Officer
@rolES: Analista Senior GRC
@cat: grc
@nivel: mid
@anos: 4-7 años
@sinonimos: Compliance Officer · Risk & Compliance Manager
@salario_mes: $2,100 - $12,500
@salario_ano: $25,000 - $150,000
@demanda: ALTA (escasez perfiles bilingües)
@remoto: Remoto disponible
@relacionados: 26, 28, 29, 30

### Descripción
Lidera auditorías, gestiona programa de compliance, hace risk assessments, presenta a management, asesora a equipos en controles, gestiona terceros (vendor risk).

### Hard Skills
- Frameworks profundos
- Third-party risk (TPRM)
- Control design
- Gap analysis
- Vendor assessments
- Regulatory mapping

### Tools
- AuditBoard
- Archer avanzado
- Vanta, Drata
- MetricStream
- OneTrust
- UpGuard, SecurityScorecard (TPRM)

### Soft Skills
- Comunicación ejecutiva
- Gestión de proyectos
- Negociación con auditores
- Pedagogía organizacional
- Gestión de stakeholders

### Certs
- CISA ⭐ (gold standard)
- CRISC
- CISM
- CCSK
- CCAK
- ISO 27001 LA

### Cómo empezar
Avanza desde GRC Junior con CISA o CRISC + experiencia liderando una auditoría completa.

### Crecimiento
GRC Manager → Director of GRC → CISO

### Mercados
USA, México, Brasil, Colombia, Chile. Bancos, fintech, SaaS, multinacionales

---

## Rol #28: IT Auditor
@rolES: Auditor de TI / Sistemas
@cat: grc
@nivel: mid
@anos: 2-8 años
@sinonimos: IT Audit Senior
@salario_mes: $1,300 - $10,000
@salario_ano: $15,600 - $120,000
@demanda: ALTA (Big4 y banca)
@remoto: Híbrido (visitas a cliente)
@relacionados: 26, 27, 31

### Descripción
Realiza auditorías de TI internas/externas, evalúa controles ITGC, ejecuta SOX testing, valida cumplimiento de políticas, emite reportes de hallazgos.

### Hard Skills
- ITGC
- SOX
- ISO 27001
- COBIT
- Sampling techniques
- Audit procedures
- Control testing
- Evidence evaluation

### Tools
- Excel avanzado
- ACL
- IDEA
- TeamMate
- Workiva
- ServiceNow GRC
- AuditBoard

### Soft Skills
- Escepticismo profesional
- Comunicación con auditados
- Independencia ética
- Escritura clara
- Gestión de proyectos cortos

### Certs
- CISA ⭐ (gold standard)
- CIA (Internal Auditor)
- CISSP
- ISO 27001 LA

### Cómo empezar
Big4 graduate program entry-level + CISA en 1-2 años.

### Crecimiento
Senior IT Auditor → Audit Manager → Internal Audit Director → CFO/Risk track

### Mercados
USA, México, Brasil, Argentina, Colombia, Chile. Big4 (Deloitte, KPMG, EY, PwC), banca, gobierno

---

## Rol #29: Cyber Risk Manager
@rolES: Gerente de Riesgo Cibernético
@cat: grc
@nivel: mid
@anos: 4-8 años
@sinonimos: Risk Analyst · IT Risk Manager
@salario_mes: $3,000 - $15,000
@salario_ano: $36,000 - $180,000
@demanda: MUY ALTA
@remoto: Remoto disponible
@relacionados: 26, 27, 36

### Descripción
Identifica, cuantifica y gestiona riesgo cibernético, hace risk assessments cuantitativos (FAIR), reporta a comité de riesgo, define apetito de riesgo con C-level.

### Hard Skills
- ISO 31000, NIST RMF, FAIR, OCTAVE
- Risk quantification
- Scenario analysis
- KRIs
- Risk reporting
- Threat modeling business-level

### Tools
- FAIR-U
- RiskLens
- Archer Risk
- ServiceNow IRM
- MetricStream
- Excel/Power BI avanzado

### Soft Skills
- Pensamiento analítico cuantitativo
- Comunicación ejecutiva
- Traducción técnico→negocio
- Presentación a Boards
- Storytelling de riesgo

### Certs
- CRISC ⭐ (gold standard)
- Open FAIR
- CISM
- ISO 31000
- CCRMP

### Cómo empezar
Desde GRC Senior/Risk Analyst tradicional + FAIR + CRISC.

### Crecimiento
Cyber Risk Director → CRO (Chief Risk Officer) o CISO

### Mercados
USA, Canadá, México, Brasil, Colombia. Bancos, seguros, gobierno, multinacionales

---

## Rol #30: Privacy Engineer / Consultant
@rolES: Ingeniero / Consultor de Privacidad
@cat: grc
@nivel: mid
@anos: 3-7 años
@sinonimos: Data Privacy Consultant
@salario_mes: $3,000 - $15,000
@salario_ano: $36,000 - $180,000
@demanda: ALTA (boom LGPD, Ley 21.719 Chile)
@remoto: Remoto disponible
@relacionados: 27, 32, 33

### Descripción
Implementa privacy by design en productos, hace DPIAs/PIAs, mapea data flows, asesora cumplimiento de GDPR/LGPD/CCPA/LFPDPPP, gestiona consentimiento y ARCO.

### Hard Skills
- GDPR, LGPD, CCPA, LFPDPPP
- Privacy by design
- Data mapping
- PIAs/DPIAs
- Anonymization/pseudonymization
- Consent management

### Tools
- OneTrust
- TrustArc
- BigID
- Securiti.ai
- Privitar
- Collibra

### Soft Skills
- Atención al detalle
- Traducción técnico-legal
- Comunicación con legal/devs/business
- Pedagogía organizacional

### Certs
- CIPP/E o CIPP/US (IAPP) ⭐
- CIPM
- CIPT
- FIP
- IAPP AIGP (AI Governance)

### Cómo empezar
Desde Legal/Compliance o desde AppSec/Engineering + CIPP/E.

### Crecimiento
Senior Privacy Engineer → Privacy Manager → DPO → CPO

### Mercados
USA, Canadá, Brasil, México, Argentina, Chile, Colombia. Multinacionales, SaaS, healthcare, retail

---

## Rol #31: ISO 27001 Lead Auditor/Implementer
@rolES: Auditor/Implementador Líder ISO 27001
@cat: grc
@nivel: mid
@anos: 3-7 años
@sinonimos: ISMS Consultant
@salario_mes: $2,100 - $11,700
@salario_ano: $25,000 - $140,000
@demanda: ALTA (camino dorado LATAM)
@remoto: Híbrido (visitas a clientes)
@relacionados: 27, 28, 40

### Descripción
Implementa o audita Sistemas de Gestión de Seguridad de la Información (SGSI), guía empresas en obtener/mantener ISO 27001, ejecuta certificaciones de tercera parte.

### Hard Skills
- ISO/IEC 27001:2022
- ISO 27002 controles
- ISO 27005 risk
- Gap analysis
- Control implementation
- SoA

### Tools
- Plantillas de SGSI
- Vanta, Drata
- Herramientas de gap analysis
- Excel para controles
- GRC platforms

### Soft Skills
- Comunicación con todos niveles
- Pedagogía organizacional
- Paciencia con procesos
- Gestión de proyectos
- Diplomacia

### Certs
- ISO 27001 Lead Implementer (PECB/BSI)
- ISO 27001 Lead Auditor (IRCA/PECB)
- CISA
- CISM

### Cómo empezar
Saca ISO 27001 LI primero, haz 2-3 implementaciones, luego LA. Freelance común.

### Crecimiento
Senior Consultant → Cybersecurity Practice Lead → vCISO

### Mercados
LATAM completo, USA. Consultoras (Big4, BDO, Mazars), certificadoras (BSI, BV, SGS), empresas en certificación

---

## Rol #32: Data Protection Officer (DPO)
@rolES: Oficial de Protección de Datos
@cat: legal
@nivel: senior
@anos: 5-10 años
@sinonimos: Encargado de Datos Personales
@salario_mes: $2,500 - $19,900
@salario_ano: $30,000 - $238,000
@demanda: MUY ALTA (obligatorio por ley)
@remoto: Híbrido / Remoto
@relacionados: 30, 33

### Descripción
Rol legal obligatorio en muchas jurisdicciones (LGPD Brasil, GDPR, Chile post-Ley 21.719). Interactúa con autoridad (ANPD, INAI, AAIP, SIC), responde derechos de titulares, supervisa DPIAs.

### Hard Skills
- Derecho de protección de datos profundo
- Privacy frameworks
- Gestión de incidentes de privacidad
- Derechos ARCO
- DPIA leadership

### Tools
- OneTrust
- TrustArc
- Herramientas legaltech
- Gestión documental
- Plataformas de consentimiento

### Soft Skills
- Comunicación legal precisa
- Independencia (rol legalmente independiente)
- Liderazgo de privacidad
- Comunicación con autoridades
- Gestión de crisis

### Certs
- CIPP/E o CIPP/US ⭐
- CIPM
- CIPT (IAPP - los 3 son el FIP)
- Lead Implementer LGPD/GDPR

### Cómo empezar
Background legal + CIPP/E + experiencia GDPR/LGPD. O perfil técnico + estudios de derecho de datos.

### Crecimiento
Senior DPO → Chief Privacy Officer (CPO) → Board Advisor

### Mercados
Brasil (LGPD lo exige), Argentina, México, Chile (Ley 21.719), Colombia. Multinacionales

---

## Rol #33: Cyber Lawyer
@rolES: Abogado en Ciberseguridad y Privacidad
@cat: legal
@nivel: senior
@anos: 5-15+ años
@sinonimos: Cybersecurity Counsel
@salario_mes: $3,300 - $20,800
@salario_ano: $40,000 - $250,000
@demanda: ALTA y creciente
@remoto: Híbrido
@relacionados: 32, 30

### Descripción
Asesoría legal en brechas de seguridad, contratos de ciberseguridad, litigios por incidentes, cumplimiento regulatorio, response legal en ransomware, M&A cyber due diligence.

### Hard Skills
- Derecho cibernético
- Privacidad de datos
- Derecho probatorio digital
- Contratos tecnológicos
- HIPAA, PCI, SOX, LGPD
- IR legal

### Tools
- Software de gestión legal
- eDiscovery (Relativity, Logikcull)
- Herramientas de chain of custody
- NDA/contract management

### Soft Skills
- Argumentación legal
- Escritura legal precisa
- Negociación
- Presentación en juicio
- Gestión de crisis

### Certs
- JD/Licenciatura en Derecho (obligatorio)
- CIPP/E o CIPP/US
- Master en Derecho Digital

### Cómo empezar
Carrera de Derecho + especialización en cyber/privacy + CIPP.

### Crecimiento
Senior Cyber Counsel → General Counsel especializado → Partner en law firm

### Mercados
USA, Brasil, México, Argentina. Firmas legales tecnológicas, in-house counsel en multinacionales

---

## Rol #34: Security Manager
@rolES: Gerente de Seguridad de la Información
@cat: leadership
@nivel: manager
@anos: 7-12 años
@sinonimos: InfoSec Manager
@salario_mes: $2,900 - $15,000
@salario_ano: $35,000 - $180,000
@demanda: ALTA (escasez de managers técnicos)
@remoto: Híbrido principalmente
@relacionados: 35, 36, 37

### Descripción
Lidera equipo de 5-20 personas (SOC, AppSec, IAM, etc), reporta a CISO/CIO, gestiona presupuesto, owner de KPIs, hiring/people management.

### Hard Skills
- Gestión de equipos técnicos
- Planificación táctica
- Frameworks de seguridad
- KPIs/OKRs
- Gestión de proveedores
- Comprensión técnica transversal

### Tools
- Jira
- Confluence
- Herramientas de PM
- Dashboards SIEM/GRC
- Power BI
- People management platforms

### Soft Skills
- Liderazgo de personas
- Mentoría y desarrollo de equipo
- Comunicación ejecutiva
- Gestión de conflictos
- Hiring
- Budget management

### Certs
- CISM ⭐ (gold standard)
- CISSP
- PMP / Scrum Master
- MBA valorado

### Cómo empezar
Promoción desde Senior técnico → Lead → Manager. CISM acelera el salto.

### Crecimiento
Director of Security → CISO

### Mercados
USA, México, Brasil, Chile, Colombia, Argentina. Cualquier empresa mediana+

---

## Rol #35: Security Program Manager
@rolES: Gerente de Programa de Seguridad
@cat: leadership
@nivel: manager
@anos: 5-10 años
@sinonimos: Security PMO
@salario_mes: $2,500 - $15,000
@salario_ano: $30,000 - $180,000
@demanda: ALTA
@remoto: Remoto disponible
@relacionados: 34, 36

### Descripción
Lidera programas/proyectos de seguridad transversales (ej: implementar Zero Trust, ISO 27001, M&A integration). No siempre people manager directo.

### Hard Skills
- Gestión de proyectos avanzada
- Planificación estratégica
- Gestión de stakeholders
- Cybersecurity frameworks
- Presupuestos
- Risk management

### Tools
- Jira
- Confluence
- MS Project
- Smartsheet
- ServiceNow
- Dashboards customs

### Soft Skills
- Gestión de stakeholders senior
- Comunicación ejecutiva
- Negociación interna
- Organización extrema
- Public speaking

### Certs
- PMP + CISSP combo gold ⭐
- CISM
- Prince2
- Lean Six Sigma
- Scrum/SAFe

### Cómo empezar
Desde PM tradicional + CISSP/CISM, o desde Security Engineer + PMP.

### Crecimiento
Senior PM → Director of Security Programs → Director of Security

### Mercados
USA, Canadá, México, Brasil. Enterprise grandes con muchos programas paralelos

---

## Rol #36: Director of Security / VP
@rolES: Director / VP de Seguridad
@cat: leadership
@nivel: executive
@anos: 10-15 años
@sinonimos: Head of Security
@salario_mes: $5,800 - $23,300
@salario_ano: $70,000 - $280,000
@demanda: ALTA en empresas grandes
@remoto: Híbrido (oficina central usual)
@relacionados: 34, 37, 38

### Descripción
Reporta a CISO o CIO/CTO, gestiona varios managers (50-200 personas en su org), define estrategia táctica, presupuesto multimillonario, owner de domains.

### Hard Skills
- Gestión de organizaciones grandes
- Presupuesto multi-millón
- Estrategia anual
- Frameworks corporativos
- Gestión de proveedores enterprise

### Tools
- Suite ejecutiva
- Dashboards de reporting
- Herramientas de finance/HR
- GRC enterprise

### Soft Skills
- Liderazgo ejecutivo
- Política organizacional
- Gestión de C-suite
- Comunicación con Board
- Hiring senior
- Crisis management

### Certs
- CISSP ⭐
- CISM
- CCISO
- MBA valorado especialmente

### Cómo empezar
Promoción desde Manager con track record sólido + CISSP + visibilidad ejecutiva.

### Crecimiento
CISO → CSO → Board roles

### Mercados
USA principalmente, México, Brasil. Enterprise grandes (Fortune 500 / equivalente LATAM)

---

## Rol #37: CISO (Chief Information Security Officer)
@rolES: Director Ejecutivo de Seguridad
@cat: leadership
@nivel: executive
@anos: 12-20+ años
@sinonimos: CSO
@salario_mes: $4,200 - $39,200
@salario_ano: $50,000 - $470,000
@demanda: ALTA (perfiles muy escasos)
@remoto: Híbrido (presencia ejecutiva)
@relacionados: 36, 38, 16

### Descripción
Estrategia de seguridad enterprise-wide, gestión de riesgo de negocio, reporta a CEO/Board, gestión de presupuesto, cumplimiento regulatorio, comunicaciones de crisis.

### Hard Skills
- Gestión estratégica empresarial
- Riesgo de negocio
- Regulación múltiple
- Política organizacional
- M&A cyber
- Board reporting
- Crisis management

### Tools
- Dashboards ejecutivos
- Herramientas de board reporting
- GRC enterprise
- Métricas cyber risk en dollars

### Soft Skills
- Liderazgo ejecutivo
- Comunicación con Board (sin tech-speak)
- Gestión política
- Visión estratégica multi-año
- Crisis pública
- Storytelling de riesgo

### Certs
- CISSP + CISM + CRISC combo ⭐
- CCISO (EC-Council)
- MBA muy valorado
- Programas ejecutivos (Harvard/Wharton)

### Cómo empezar
Track de 10-15 años + CISSP + visibilidad pública + idealmente MBA. vCISO como puente.

### Crecimiento
CSO / Chief Risk Officer → Board Director → Founder de consultora

### Mercados
USA (mejor pagado), México, Brasil, Chile (Ley 21.663), Argentina. Bancos top, fintechs unicornio, multinacionales

---

## Rol #38: vCISO (Virtual / Fractional)
@rolES: CISO Virtual / Fraccional
@cat: leadership
@nivel: executive
@anos: 10+ años
@sinonimos: Fractional CISO
@salario_mes: $5,000 - $29,200 (variable)
@salario_ano: $60,000 - $350,000
@demanda: ALTA y creciente en LATAM
@remoto: 100% Remoto
@relacionados: 37, 31, 40

### Descripción
Sirve como CISO part-time/fraccional para PyMEs y mid-market que no pueden pagar CISO full-time. Modelo creciente en LATAM. 3-8 clientes simultáneos típicos.

### Hard Skills
- Mismo set que CISO
- Experiencia multi-industria
- Onboarding rápido
- Gestión multi-cliente
- Ventas de servicios

### Tools
- Mismas que CISO
- Herramientas de consultoría
- Proposals, time tracking
- Multi-tenant dashboards

### Soft Skills
- Adaptabilidad multi-cliente
- Ventas técnicas
- Gestión multi-stakeholder
- Comunicación con CEOs PyME
- Mentoría rápida
- Gestión de propio negocio

### Certs
- CISSP, CISM, CCISO ⭐
- Reputación pública
- Idealmente experiencia previa como CISO full-time

### Cómo empezar
Después de ser CISO full-time, transición a freelance con red de contactos.

### Crecimiento
Founder de boutique de consultoría → Board Director (múltiples boards)

### Mercados
USA grandes; LATAM creciendo fuerte (México, Brasil, Argentina, Chile). PyMEs reguladas (fintech, salud)

---

## Rol #39: Security Sales Engineer / Presales
@rolES: Ingeniero de Preventa de Ciberseguridad
@cat: sales
@nivel: mid
@anos: 3-8 años
@sinonimos: Solutions Engineer
@salario_mes: $3,300 - $26,900
@salario_ano: $40,000 - $322,000
@demanda: MUY ALTA (técnico + soft skills)
@remoto: Remoto con viajes ocasionales
@relacionados: 11, 40, 41

### Descripción
Hace demos técnicas, lidera POCs (Proof of Concept), responde RFPs/RFIs, traduce features de producto a valor de negocio, soporta al sales team, evangeliza tecnología.

### Hard Skills
- Conocimiento profundo del producto vendido
- Arquitecturas de seguridad
- Integraciones
- Troubleshooting
- ROI calculation

### Tools
- Demo environments
- Demostack/Reprise
- Salesforce (CRM)
- POC tracking
- Producto del vendor

### Soft Skills
- Storytelling técnico
- Presentación a audiencias mixtas
- Comunicación bilingüe (técnico+business)
- Empatía con cliente
- Gestión de objeciones
- Energía

### Certs
- Certificaciones del producto (vendor-specific)
- CISSP valorado
- Certs de cloud para contexto

### Cómo empezar
Desde Security Engineer + soft skills + inglés. Empezar como Associate SE.

### Crecimiento
Senior SE → SE Manager → Director of SE → Field CTO

### Mercados
USA, Canadá (mejores comisiones), México, Brasil, Argentina, Colombia, Chile. Vendors: Cisco, Palo Alto, CrowdStrike, Fortinet, Microsoft, AWS, Wiz

---

## Rol #40: Security Consultant / Advisory
@rolES: Consultor de Ciberseguridad
@cat: sales
@nivel: mid
@anos: 1-15+ años
@sinonimos: Big4 Cyber Consultant
@salario_mes: $1,250 - $12,500
@salario_ano: $15,000 - $150,000+
@demanda: ALTA (Big4 contratan continuamente)
@remoto: Híbrido (viajes a cliente)
@relacionados: 27, 31, 38, 41

### Descripción
Asesora a clientes en estrategia, implementaciones, auditorías, transformaciones. En Big4 (Deloitte, KPMG, EY, PwC), Accenture, IBM, Capgemini.

### Hard Skills
- Frameworks múltiples
- Technical breadth amplia
- Business acumen
- Industry knowledge
- Methodology

### Tools
- MS Office avanzado
- Herramientas internas de la firma
- Visio
- Frameworks templates

### Soft Skills
- Comunicación ejecutiva
- Presentación a C-level
- Hot delivery
- Gestión de cliente difícil
- Viajes constantes
- Escritura técnico/ejecutiva
- Vendedor implícito

### Certs
- CISSP, CISM, CISA, CCSP
- Para entrada Big4: Security+ + degree
- Certs específicas por práctica

### Cómo empezar
Big4 graduate programs (entry-level), o lateral desde industria.

### Crecimiento
Senior Consultant → Manager → Senior Manager → Director → Partner

### Mercados
USA, México, Brasil, Argentina, Colombia, Chile. Big4 + Accenture + IBM + Capgemini + boutiques

---

## Rol #41: Solutions Architect (Vendor)
@rolES: Arquitecto de Soluciones (Vendor)
@cat: sales
@nivel: senior
@anos: 7-12 años
@sinonimos: Field SA · Principal SE
@salario_mes: $5,000 - $23,300
@salario_ano: $60,000 - $280,000
@demanda: ALTA en vendors grandes
@remoto: Híbrido (viajes a cliente)
@relacionados: 39, 40, 15

### Descripción
Trabaja con grandes cuentas estratégicas pre/post-venta, diseña arquitecturas complejas usando productos del vendor, lidera POCs multi-producto.

### Hard Skills
- Producto del vendor a nivel maestro
- Arquitecturas enterprise
- Integraciones complejas
- Cloud y on-prem
- Scripting/automation
- L3+ troubleshooting

### Tools
- Herramientas del vendor
- Lab environments
- Automation tooling
- Monitoring del producto en cliente

### Soft Skills
- Liderazgo técnico de account team
- Comunicación con CTOs/CISOs cliente
- Project leadership
- Mentoría a SEs
- Escritura técnica

### Certs
- Certificaciones del vendor a niveles top
- CISSP

### Cómo empezar
Desde Senior SE + certificaciones top del producto + grandes cuentas owned.

### Crecimiento
Principal SA → SA Manager → Field CTO

### Mercados
USA, México, Brasil. Vendors top (Palo Alto, Cisco, CrowdStrike, Microsoft, AWS, Wiz)

---

## Rol #42: Security Awareness Specialist
@rolES: Especialista en Concientización
@cat: awareness
@nivel: mid
@anos: 2-6 años
@sinonimos: Cyber Culture Specialist
@salario_mes: $1,250 - $17,400
@salario_ano: $15,000 - $209,000
@demanda: ALTA (factor humano #1)
@remoto: Remoto disponible
@relacionados: 43, 47

### Descripción
Diseña y ejecuta programa de awareness corporativo: campañas de phishing simulado, contenido educativo, gamificación, capacitación, medición de KPIs.

### Hard Skills
- Adult learning theory
- Security fundamentals
- Phishing techniques (para simular)
- Métricas de comportamiento
- Behavior change
- Marketing interno

### Tools
- KnowBe4 ⭐ (líder)
- Cofense PhishMe
- Proofpoint Security Awareness
- Hoxhunt
- Living Security
- Articulate

### Soft Skills
- Comunicación creativa
- Escritura accesible
- Diseño básico
- Paciencia con usuarios no técnicos
- Pedagogía
- Empatía
- Creatividad
- Sentido del humor

### Certs
- Security+
- SANS SACP
- KnowBe4 Certified
- IAB Security Awareness Practitioner

### Cómo empezar
Desde marketing, educación, comunicación, RRHH + Security+. Excelente para career changers.

### Crecimiento
Senior Awareness → Awareness Manager → Director of Security Culture

### Mercados
USA, Canadá, México, Brasil. Cualquier empresa con +500 empleados regulados

---

## Rol #43: Cybersecurity Trainer / Instructor
@rolES: Instructor de Ciberseguridad
@cat: awareness
@nivel: mid
@anos: 5+ años técnicos
@sinonimos: Bootcamp Instructor
@salario_mes: $1,250 - $11,700
@salario_ano: $15,000 - $140,000
@demanda: MEDIA-ALTA + boom de content creators
@remoto: 100% remoto en plataformas
@relacionados: 42, 49

### Descripción
Enseña ciberseguridad en bootcamps (Coursera, Cybrary, INE, HTB Academy, Platzi, Coderhouse), universidades, corporate training. Crea contenido educativo.

### Hard Skills
- Dominio profundo del tema enseñado
- Instructional design
- Virtualización (labs)
- Creación de contenido
- Public speaking

### Tools
- LMS (Moodle, Canvas)
- Camtasia
- OBS Studio
- Lab platforms (HTB, THM, INE)

### Soft Skills
- Pedagogía
- Paciencia
- Public speaking
- Storytelling
- Empatía con estudiantes
- Comunicación clara
- Energía sostenida
- Mentoría

### Certs
- Las del tema enseñado a nivel maestro
- Certs de instructional design valoradas

### Cómo empezar
Después de 5+ años técnicos + crear contenido educativo gratis (YouTube, TikTok, blog).

### Crecimiento
Lead Instructor → Curriculum Director → Founder de academia → Content Creator independiente (TikTok/YouTube)

### Mercados
Global. Plataformas online (Coursera, Udemy, Cybrary, INE, HTB), bootcamps (Platzi, Coderhouse, Le Wagon), universidades

---

## Rol #44: Vulnerability Management Analyst
@rolES: Analista de Gestión de Vulnerabilidades
@cat: operations
@nivel: mid
@anos: 2-5 años
@sinonimos: VM Analyst
@salario_mes: $1,300 - $18,100
@salario_ano: $15,600 - $218,000
@demanda: ALTA (rol troncal)
@remoto: Remoto disponible
@relacionados: 1, 45, 46

### Descripción
Opera scanners de vulnerabilidades, prioriza con CVSS+EPSS, coordina parches con TI, gestiona excepciones, reporta a management.

### Hard Skills
- CVSS scoring
- EPSS
- CVE management
- Network scanning
- Patch management
- Vulnerability prioritization
- Risk-based VM

### Tools
- Tenable Nessus / Tenable.io
- Qualys VMDR ⭐
- Rapid7 InsightVM
- Microsoft Defender VM
- Wiz
- Snyk

### Soft Skills
- Atención al detalle
- Comunicación con IT/devs
- Gestión de prioridades
- Paciencia con procesos de patching

### Certs
- CompTIA Security+
- Qualys VMDR
- Tenable certifications
- CySA+
- GIAC GEVA

### Cómo empezar
Desde SOC / Sysadmin + certificación de Tenable o Qualys.

### Crecimiento
Senior VM → VM Manager → Detection Engineering Lead

### Mercados
USA, México, Brasil, Colombia, Chile. Bancos, multinacionales, healthcare, todo regulado

---

## Rol #45: Endpoint Security / Patch Admin
@rolES: Administrador de Endpoint Security
@cat: operations
@nivel: junior
@anos: 1-4 años
@sinonimos: Patch Manager
@salario_mes: $1,000 - $6,700
@salario_ano: $12,000 - $80,000
@demanda: ALTA (entry-level decente)
@remoto: Híbrido
@relacionados: 1, 44, 46

### Descripción
Despliega parches a endpoints/servidores, gestiona EDR/AV en escala, hace hardening, mantiene baseline de configuración, troubleshooting de despliegues.

### Hard Skills
- Windows/Linux administration
- GPOs
- Configuración de EDR
- PowerShell/Bash
- Patch management workflows
- Image management

### Tools
- Microsoft Defender
- CrowdStrike
- SentinelOne
- Carbon Black
- Tanium
- BigFix
- MECM (SCCM)
- Intune
- Jamf (Mac)

### Soft Skills
- Atención al detalle
- Comunicación con usuarios afectados
- Paciencia con troubleshooting
- Gestión de cambios
- Documentación

### Certs
- CompTIA Security+
- MD-102 (Microsoft Endpoint)
- CrowdStrike certifications
- Tanium certifications

### Cómo empezar
Sysadmin junior + Security+ + dominio de un EDR.

### Crecimiento
Senior Endpoint Admin → Endpoint Security Engineer → Security Engineer

### Mercados
USA, México, Brasil. Cualquier enterprise con muchos endpoints

---

## Rol #46: IAM Operations / PAM Admin
@rolES: Administrador de IAM/PAM
@cat: operations
@nivel: mid
@anos: 2-5 años
@sinonimos: Identity Operations
@salario_mes: $1,500 - $9,200
@salario_ano: $18,000 - $110,000
@demanda: MUY ALTA en banca LATAM
@remoto: Híbrido
@relacionados: 18, 27, 44

### Descripción
Opera plataformas IAM/PAM día a día: provisiona/desprovisiona accesos, gestiona cuentas privilegiadas en CyberArk/BeyondTrust, hace recertificaciones, soporta auditorías.

### Hard Skills
- Active Directory
- LDAP
- IAM lifecycle
- PAM workflows
- Vaulting
- Password rotation
- Session recording
- Identity governance

### Tools
- CyberArk PAS ⭐
- BeyondTrust
- Okta
- SailPoint
- Microsoft Entra
- HashiCorp Vault
- Delinea (Thycotic)

### Soft Skills
- Atención meticulosa al detalle
- Comunicación con HR/auditores/IT
- Documentación
- Paciencia con processes de aprobación
- Ownership

### Certs
- CyberArk Defender + Sentry ⭐
- BeyondTrust certifications
- Okta certifications
- SailPoint engineer

### Cómo empezar
Sysadmin / AD admin + cert de CyberArk Defender.

### Crecimiento
Senior IAM Ops → IAM Engineer → IAM Architect

### Mercados
México, Brasil, Colombia, Chile (banca top), USA. Bancos, healthcare, enterprise grandes

---

## Rol #47: Cybersecurity Technical Writer
@rolES: Redactor Técnico de Ciberseguridad
@cat: ecosystem
@nivel: mid
@anos: 3-7 años
@sinonimos: Security Content Writer
@salario_mes: $1,250 - $10,800
@salario_ano: $15,000 - $130,000
@demanda: MEDIA-ALTA + freelance international
@remoto: 100% remoto + freelance común
@relacionados: 42, 43

### Descripción
Crea documentación técnica, whitepapers, blogs, RFP responses, knowledge bases, playbooks, manuales de producto. Vendors, consultoras, in-house, freelance.

### Hard Skills
- Escritura técnica avanzada
- Comprensión profunda de cyber (todos los dominios)
- SEO básico
- Markdown
- Docs-as-code

### Tools
- Google Docs
- MS Word
- Madcap Flare
- Notion
- GitBook
- Hugo/Jekyll/Docusaurus
- Grammarly
- Hemingway

### Soft Skills
- Escritura excepcional
- Capacidad de entrevistar expertos técnicos
- Autoaprendizaje rápido
- Atención al detalle
- Gestión de deadlines
- Adaptabilidad de voz/tono

### Certs
- Security+ (credibilidad técnica)
- Society for Technical Communication
- Certs específicas del área que escribe

### Cómo empezar
Desde periodismo / inglés / TI + Security+ + portfolio público de blogs.

### Crecimiento
Senior TW → Content Manager → Head of Content → Independent consultant

### Mercados
USA principalmente (mejores tarifas), pero freelance global. Vendors top, blogs grandes (Dark Reading, BleepingComputer)

---

## Rol #48: Cybersecurity Recruiter
@rolES: Reclutador Especializado en Ciberseguridad
@cat: ecosystem
@nivel: mid
@anos: 3-10 años
@sinonimos: Talent Acquisition - Security
@salario_mes: $1,700 - $15,000
@salario_ano: $20,000 - $180,000
@demanda: ALTA (escasez de candidatos = recruiters bien pagados)
@remoto: Remoto frecuente
@relacionados: 42, 43

### Descripción
Recluta talento de ciberseguridad para empresas. Agencias (Hays, Robert Half, PageGroup, Michael Page, Stott and May) o in-house. Headhunting de roles senior.

### Hard Skills
- Conocimiento profundo del mercado cyber
- Comprensión técnica del rol
- Boolean search
- ATS
- Sourcing
- Salary benchmarking

### Tools
- LinkedIn Recruiter ⭐
- Lever
- Greenhouse
- Workable
- Bullhorn
- hireEZ
- SeekOut
- AmazingHiring
- Gem

### Soft Skills
- Comunicación excepcional
- Networking
- Persuasión
- Ventas
- Empatía
- Leer perfiles técnicos sin ser técnico
- Pipeline management
- Resilience

### Certs
- AIRS Certified (CIR, CDSP)
- LinkedIn Recruiter cert
- CompTIA Security+ valorado

### Cómo empezar
Desde recruiter generalist + interés en tech + aprender vocabulario de cyber.

### Crecimiento
Senior Recruiter → Recruiting Manager → Head of Talent (cyber-focused)

### Mercados
USA, Canadá, México, Brasil. Agencias especializadas + in-house en cyber-first companies

---

## Rol #49: Cybersecurity Product Manager
@rolES: Product Manager de Ciberseguridad
@cat: ecosystem
@nivel: senior
@anos: 5-10 años
@sinonimos: Security PM
@salario_mes: $5,000 - $20,800
@salario_ano: $60,000 - $250,000
@demanda: ALTA en vendors top
@remoto: Remoto disponible
@relacionados: 39, 41, 43

### Descripción
Define producto y roadmap en vendors de ciberseguridad. Customer research, priorización de features, lidera equipos cross-funcionales (eng, design, marketing).

### Hard Skills
- Product management framework (lean, agile)
- Customer development
- Market research
- Métricas (NPS, MRR, retention)
- Comprensión técnica profunda del dominio

### Tools
- Productboard
- Aha!
- Jira
- Figma
- Mixpanel
- Amplitude
- Linear
- Notion
- Looker/Tableau

### Soft Skills
- Liderazgo de influencia
- Comunicación cross-team
- Storytelling
- Priorización ruthless
- Escritura de specs claros
- Presentación a ejecutivos
- Customer empathy

### Certs
- PSPO, CSPO
- Pragmatic Marketing
- CISSP o CCSP para credibilidad técnica

### Cómo empezar
Desde Security Engineer + cursos de PM, o desde PM general + aprender cyber profundo.

### Crecimiento
Senior PM → Group PM → VP of Product → CPO

### Mercados
USA (mejor pagado), Brasil, México. Big Tech, vendors top de cyber, scaleups

---

## Rol #50: Threat Researcher (Vendor)
@rolES: Investigador de Amenazas (Vendor)
@cat: ecosystem
@nivel: senior
@anos: 5-12 años
@sinonimos: Security Researcher · Threat Analyst Senior
@salario_mes: $5,000 - $20,800
@salario_ano: $60,000 - $250,000
@demanda: ALTA pero pocas posiciones
@remoto: Remoto total común
@relacionados: 5, 6, 10

### Descripción
Investiga amenazas emergentes en vendors top (Mandiant, Unit 42, Talos, CrowdStrike Intelligence, Kaspersky GReAT, ESET LATAM). Publica reportes, presenta en conferencias.

### Hard Skills
- Reverse engineering
- Malware analysis
- Threat hunting
- OSINT
- Attribution analysis
- Python
- Publicación académica/técnica

### Tools
- IDA Pro
- Ghidra
- Cuckoo
- MISP
- Maltego
- Herramientas internas del vendor
- Lab environments

### Soft Skills
- Escritura técnica de alto nivel
- Public speaking en conferencias (DEF CON, Black Hat, BSides)
- Branding personal
- Networking en industria
- Autoaprendizaje

### Certs
- OSCP
- GREM
- GCTI
- Reputación pública > certs

### Cómo empezar
Desde Malware Analyst/RE/Senior Threat Hunter + reputación pública (blog, conferencias).

### Crecimiento
Principal Researcher → Distinguished Researcher → Head of Research

### Mercados
USA principalmente, Argentina (ESET LATAM), Brasil. Vendors top: Mandiant, Unit 42, Talos, CrowdStrike, Kaspersky GReAT

**Tags:** #mcp #recursos #glosario #comunidad #documentacion

> [!info] Navegación
> ◀ Anterior: [[📂MCP/06 - Cómo Crear un Servidor MCP en Python|Crear un Servidor]]

---

# 07 — Recursos, Enlaces y Comunidad MCP

> [!quote] Referencias
> Todo lo que necesitas para seguir aprendiendo y mantenerte actualizado sobre el ecosistema MCP.

---

## 📚 Documentación y Repositorios Oficiales

| Recurso | URL | Descripción |
| :--- | :--- | :--- |
| **Especificación oficial** | [modelcontextprotocol.io](https://modelcontextprotocol.io) | Documentación completa del protocolo, guías y tutoriales |
| **Repositorio GitHub** | [github.com/modelcontextprotocol](https://github.com/modelcontextprotocol) | SDKs oficiales (Python, TypeScript, Java, C#, Kotlin), Inspector y especificación |
| **SDK Python** | [github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | El SDK de Python con `FastMCP` |
| **SDK TypeScript** | [github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | El SDK de TypeScript/Node.js |
| **Servidores oficiales** | [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Lista curada de servidores MCP de referencia |
| **MCP Inspector** | Incluido en los SDKs | Herramienta de depuración visual para probar servidores en el navegador |

---

## 🗂️ Directorios de Servidores MCP

Sitios web donde encontrar servidores MCP creados por la comunidad y empresas:

| Directorio | URL | Descripción |
| :--- | :--- | :--- |
| **mcp.so** | [mcp.so](https://mcp.so) | Directorio comunitario con cientos de servidores clasificados por categoría |
| **Glama.ai MCP** | [glama.ai/mcp](https://glama.ai/mcp) | Directorio visual con descripciones y documentación de cada servidor |
| **Smithery.ai** | [smithery.ai](https://smithery.ai) | Marketplace de servidores MCP con instalación en un clic |

---

## 🏛️ Gobernanza y Estándar Abierto

| Aspecto | Detalle |
| :--- | :--- |
| **Creador original** | **Anthropic** (creadores de Claude) — finales de 2024 |
| **Gobernanza actual** | Cedido a la **Linux Foundation** bajo la **Agentic AI Foundation** |
| **Licencia** | Código abierto (Open Source) |
| **Protocolo base** | **JSON-RPC 2.0** sobre STDIO o HTTP |
| **Adopción empresarial** | Microsoft, Google (ADK), Amazon, OpenAI, Anthropic, y cientos más |

> [!tip] ¿Por qué importa que sea de la Linux Foundation?
> Al estar bajo la Linux Foundation (la misma organización detrás de Linux, Kubernetes, Node.js...), MCP tiene garantía de:
> - **Neutralidad:** Ninguna empresa puede controlar el estándar en su beneficio
> - **Continuidad:** El protocolo seguirá evolucionando aunque Anthropic cambie de estrategia
> - **Confianza empresarial:** Las grandes empresas adoptan estándares de la Linux Foundation con más seguridad

---

## 📖 Glosario de Términos Clave

| Término | Definición | Nota Relacionada |
| :--- | :--- | :--- |
| **Host** | La aplicación donde trabaja el usuario (IDE, chatbot) | [[📂MCP/02 - Arquitectura Host Cliente y Servidor\|Arquitectura]] |
| **Client** | Componente interno del Host que habla protocolo MCP | [[📂MCP/02 - Arquitectura Host Cliente y Servidor\|Arquitectura]] |
| **Server** | Proceso independiente con acceso a la herramienta real | [[📂MCP/02 - Arquitectura Host Cliente y Servidor\|Arquitectura]] |
| **Tool** | Función ejecutable por el LLM (verbo/acción) | [[📂MCP/03 - Primitivos de MCP Tools Resources y Prompts\|Primitivos]] |
| **Resource** | Dato de solo lectura que aporta contexto | [[📂MCP/03 - Primitivos de MCP Tools Resources y Prompts\|Primitivos]] |
| **Prompt** | Plantilla predefinida de prompt reutilizable | [[📂MCP/03 - Primitivos de MCP Tools Resources y Prompts\|Primitivos]] |
| **STDIO** | Transporte local (entrada/salida estándar del SO) | [[📂MCP/02 - Arquitectura Host Cliente y Servidor\|Arquitectura]] |
| **HTTP/SSE** | Transporte remoto (HTTP con Server-Sent Events) | [[📂MCP/02 - Arquitectura Host Cliente y Servidor\|Arquitectura]] |
| **JSON-RPC** | Protocolo de comunicación base de MCP (peticiones/respuestas en JSON) | [[📂MCP/01 - Qué es MCP y Problema que Resuelve\|Fundamentos]] |
| **FastMCP** | Abstracción de alto nivel del SDK Python para crear servidores rápidamente | [[📂MCP/06 - Cómo Crear un Servidor MCP en Python\|Crear Servidor]] |
| **MCP Inspector** | Herramienta de depuración visual para probar servidores en el navegador | [[📂MCP/06 - Cómo Crear un Servidor MCP en Python\|Crear Servidor]] |
| **OAuth** | Protocolo de autenticación usado para MCPs remotos (HTTP) | [[📂MCP/04 - Cómo Conectar y Utilizar Servidores MCP\|Conexión]] |

---

## 🔗 Conexiones con Otros Módulos de la Bóveda

MCP es un protocolo transversal que conecta con múltiples áreas de tu bóveda:

- **IA Generativa y Agentes:** [[📂AWS/📂IA Practitioner/📂M3 - IA Generativa/10 - Agentes de IA y MCP|Agentes de IA y MCP (AWS)]] — MCP en el contexto específico de Amazon Bedrock y la certificación AIF-C01.
- **Prompt Engineering:** [[📂AWS/📂IA Practitioner/📂M3 - IA Generativa/12 - Técnicas de Prompt Engineering|Técnicas de Prompt Engineering]] — Los Prompt Templates de MCP se relacionan directamente con el Prompt Engineering.
- **Foundation Models:** [[📂AWS/📂IA Practitioner/📂M3 - IA Generativa/01 - Foundation Models vs Narrow AI|Foundation Models]] — Los FMs son los "cerebros" que MCP conecta con el mundo real.
- **Docker:** [[🐳 Índice - Guía Docker|Docker]] — Los servidores MCP se pueden contenizar y desplegar como contenedores Docker.
- **Git:** [[Fundamentos Git|Git y GitHub]] — GitHub fue una de las primeras integraciones MCP oficiales.

---
→ Volver al índice: [[📂MCP/00 - MOC MCP|🔌 MOC MCP]]

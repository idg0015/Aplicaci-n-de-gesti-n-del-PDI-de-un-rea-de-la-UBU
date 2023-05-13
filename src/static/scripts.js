$(document).ready(function () {
    if (document.getElementById('tablaCentros') != null) {
        let formURL = "{{ url_for('centro_bp.form_centro') }}";
        new gridjs.Grid({
            columns: [
                {
                    name: 'Id',
                    hidden: true
                },
                {
                    id: 'codigo',
                    name: 'Código interno',
                    attributes: {style: 'text-align: center!important;'},
                },
                "Nombre",
                {
                    id: "abreviatura",
                    name: "Abreviatura",
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    id: 'email',
                    name: 'Email administrativo'
                },
                {
                    name: 'Acciones',
                    attributes: {style: 'text-align: center!important;'},
                    sort: false,
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="/centros/${row.cells[0].data}"><i class="bi bi-pencil-square"></i></a> <a href="/centros/eliminar/${row.cells[0].data}" class="icono" onclick="return confirm('¿Está seguro de eliminar el centro? No se podrá eliminar si tiene alguna titulación vinculada')"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            className: {
                // td: "text-center",
                th: "text-center"
            },
            language: gridjs.l10n.esES,
            sort: true,
            search: true,
            width: "70%",
            data: centros
        }).render(document.getElementById("tablaCentros"));
    }

    if (document.getElementById('tablaTitulaciones') != null) {
        new gridjs.Grid({
            columns: [
                {
                    name: 'Id',
                    hidden: true
                },
                {
                    id: 'codigo',
                    name: 'Código interno',
                    attributes: {style: 'text-align: center!important;'},
                },
                "Nombre",
                {
                    id: "abreviatura",
                    name: "Abreviatura",
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    name: 'URL',
                    sort: false,
                    formatter: (_, row) => gridjs.html(`<a href='${row.cells[3].data}' class="enlace">Web</a>`),
                    attributes: {style: 'text-align: center!important;'},
                },
                "Centro",
                {
                    name: 'Acciones',
                    attributes: {style: 'text-align: center!important;'},
                    sort: false,
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="/titulaciones/${row.cells[0].data}"><i class="bi bi-pencil-square"></i></a> <a href="/titulaciones/eliminar/${row.cells[0].data}" class="icono" onclick="return confirm('¿Está seguro de eliminar la titulación? Se eliminarán sus asignaturas asociadas y todo lo que dependa de estas.')"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            className: {
                th: "text-center"
            },
            width: "95%",
            language: gridjs.l10n.esES,
            sort: true,
            search: true,
            resizable: true,
            pagination: {
                limit: 7
            },
            data: titulaciones
        }).render(document.getElementById("tablaTitulaciones"));
    }

    if (document.getElementById('tablaAsignaturas') != null) {
        new gridjs.Grid({
            columns: [
                {
                    name: 'Id',
                    hidden: true
                },
                {
                    id: 'codigo',
                    name: 'Código interno',
                    attributes: {style: 'text-align: center!important;'},
                },
                "Nombre",
                {
                    id: 'tipo',
                    name: 'Tipo',
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    id: 'titulacion',
                    name: 'Titulación'
                },
                {
                    id: 'creditos_teoria',
                    name: 'Créditos teoría',
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    id: 'creditos_practica',
                    name: 'Créditos práctica',
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    id: 'curso',
                    name: 'Curso',
                    attributes: {style: 'text-align: center!important;'}
                },
                {
                    id: 'semestre',
                    name: 'Semestre',
                    attributes: {style: 'text-align: center!important;'}
                },
                "Abreviaturas",
                {
                    name: 'Acciones',
                    sort: false,
                    attributes: {style: 'text-align: center!important;'},
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="/asignaturas/${row.cells[0].data}"><i class="bi bi-pencil-square"></i></a> <a href="/asignaturas/eliminar/${row.cells[0].data}" class="icono" onclick="return confirm('¿Está seguro de eliminar la asignatura? Se eliminarán sus abreviaturas asociadas y los cursos donde se encuentren.')"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            className: {
                th: "text-center"
            },
            width: "95%",
            language: gridjs.l10n.esES,
            sort: true,
            search: true,
            resizable: true,
            pagination: {
                limit: 7
            },
            data: asignaturas
        }).render(document.getElementById("tablaAsignaturas"));
    }

    if (document.getElementById('tablaDocentes') != null) {
        new gridjs.Grid({
            columns: [
                {
                    name: 'Id',
                    hidden: true
                },
                "Nombre", "Apellidos", "Email",
                {
                    id: 'reducciones',
                    name: 'Reducciones',
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    name: 'Acciones',
                    sort: false,
                    attributes: {style: 'text-align: center!important;'},
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="/docentes/${row.cells[0].data}"><i class="bi bi-pencil-square"></i></a> <a href="/docentes/eliminar/${row.cells[0].data}" class="icono" onclick="return confirm('¿Está seguro de eliminar el docente?')"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            className: {
                th: "text-center"
            },
            language: gridjs.l10n.esES,
            sort: true,
            search: true,
            width: "70%",
            data: docentes
        }).render(document.getElementById("tablaDocentes"));
    }

    if (document.getElementById('tablaPlazas') != null) {
        new gridjs.Grid({
            columns: [
                {
                    name: 'Id',
                    hidden: true
                },
                {
                    id: 'nombre',
                    name: 'Nombre'
                },
                {
                    id: "rpt",
                    name: gridjs.html('<span title="Relación Puestos de Trabajo (RPT)">RPT</span>'),
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    id: 'fecha_incorporacion',
                    name: gridjs.html('<span title="Fecha incorporación">Fecha incorporación</span>'),
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    id: 'fecha_cese',
                    name: gridjs.html('<span title="Fecha cese">Fecha cese</span>'),
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    id: 'num_concursos_contratacion',
                    name: gridjs.html('<span title="Número concursos contratación">Nº C.C</span>'),
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    id: 'docente',
                    name: 'Docente',
                },
                {
                    id: 'tipo_contrato',
                    name: 'Tipo Contrato',
                },
                {
                    name: 'Acciones',
                    sort: false,
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="/plazas/${row.cells[0].data}"><i class="bi bi-pencil-square"></i></a> <a href="/plazas/eliminar/${row.cells[0].data}" class="icono" onclick="return confirm('¿Está seguro de eliminar la plaza? Se eliminarán sus relaciones con grupos.')"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            language: gridjs.l10n.esES,
            sort: true,
            search: true,
            width: "70%",
            className: {
                th: "text-center"
            },
            data: plazas
        }).render(document.getElementById("tablaPlazas"));
    }

    if (document.getElementById('tablaContratos') != null) {
        new gridjs.Grid({
            columns: [
                {
                    name: 'Id',
                    hidden: true
                },
                {
                    id: 'nombre',
                    name: 'Nombre',
                },
                {
                    id: 'abreviatura',
                    name: 'Abreviatura',
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    id: 'capacidad_anual',
                    name: 'Capacidad anual (horas)',
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    name: 'Acciones',
                    sort: false,
                    attributes: {style: 'text-align: center!important;'},
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="/contratos/${row.cells[0].data}"><i class="bi bi-pencil-square"></i></a> <a href="/contratos/eliminar/${row.cells[0].data}" class="icono" onclick="return confirm('¿Está seguro de eliminar el tipo de contrato? Se eliminarán las plazas asociadas y todo lo que dependa de ellas.')"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            language: gridjs.l10n.esES,
            sort: true,
            search: true,
            width: "70%",
            className: {
                th: "text-center"
            },
            data: contratos
        }).render(document.getElementById("tablaContratos"));
    }

    if (document.getElementById('tablaAreas') != null) {
        new gridjs.Grid({
            columns: [
                {
                    name: 'Id',
                    hidden: true
                },
                "Nombre", "Abreviatura", "Departamento",
                {
                    name: 'Acciones',
                    sort: false,
                    attributes: {style: 'text-align: center!important;'},
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="/areas/${row.cells[0].data}"><i class="bi bi-pencil-square"></i></a> <a href="/areas/eliminar/${row.cells[0].data}" class="icono" onclick="return confirm('¿Está seguro de eliminar el área? Se eliminarán las plazas asociadas y todo lo que dependa de ellas.')"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            language: gridjs.l10n.esES,
            sort: true,
            search: true,
            width: "70%",
            className: {
                th: "text-center"
            },
            data: areas
        }).render(document.getElementById("tablaAreas"));
    }

    if (document.getElementById('tablaDepartamentos') != null) {
        new gridjs.Grid({
            columns: [
                {
                    name: 'Id',
                    hidden: true
                },
                "Nombre",
                {
                    id: 'abreviatura',
                    name: 'Abreviatura',
                    attributes: {style: 'text-align: center!important;'},
                },
                {
                    name: 'Acciones',
                    sort: false,
                    attributes: {style: 'text-align: center!important;'},
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="/departamentos/${row.cells[0].data}"><i class="bi bi-pencil-square"></i></a> <a href="/departamentos/eliminar/${row.cells[0].data}" class="icono" onclick="return confirm('¿Está seguro de eliminar el departamento? Se eliminarán sus áreas y todo lo relacionado con ellas.')"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            language: gridjs.l10n.esES,
            sort: true,
            search: true,
            width: "70%",
            className: {
                th: "text-center"
            },
            data: departamentos
        }).render(document.getElementById("tablaDepartamentos"));
    }

    if (document.getElementById('tablaCursos') != null) {
        new gridjs.Grid({
            columns: [
                {
                    name: 'Id',
                    hidden: true
                },
                {
                    id: "ano_inicio",
                    name: gridjs.html('<span title="Año inicio">Año inicio</span>'),
                },
                {
                    id: "ano_fin",
                    name: gridjs.html('<span title="Año fin">Año fin</span>'),
                },
                {
                    name: 'Acciones',
                    sort: false,
                    formatter: (_, row) => gridjs.html(`<a href="#" class="icono" title="Modificar curso" data-bs-toggle="modal" data-bs-target="#year-modal" onclick="getId(${row.cells[0].data})"><i class="bi bi-calendar-date-fill"></i></a>
                    <a class="icono" href="#" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-pencil-square"></i></a>
                    <a class="icono" href="/cursos/duplicar/${row.cells[0].data}" onclick="return confirm('¿Está seguro de duplicar el curso? Se creará un curso con el año de inicio ${parseInt(row.cells[1].data) + 1}')"><i class="bi bi-clipboard-plus-fill"></i></a>
                    <a href="/cursos/eliminar/${row.cells[0].data}" class="icono" title="Eliminar" onclick="return confirm('¿Está seguro de eliminar el curso? Se eliminarán todas las relaciones de asignaturas y sus grupos.')"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            className: {
                td: "text-center",
                th: "text-center"
            },
            language: gridjs.l10n.esES,
            sort: true,
            search: true,
            width: "70%",
            data: cursos
        }).render(document.getElementById("tablaCursos"));
    }

    if (document.getElementById('tablaGrupos') != null) {
        new gridjs.Grid({
            columns: [
                "Centro", "Titulación", "Asignatura", "Semestre", "Nº grupos teoría", "Nº grupos práctica", "Nº grupos online teoría", "Nº grupos online práctica", "Nº grupos inglés teoría", "Nº grupos inglés práctica",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<button type="button" class="btn btn-primary" onclick="alert( '${row.cells[0].data}');">Gestionar grupos</button>`)
                },
            ],
            language: gridjs.l10n.esES,
            sort: true,
            search: true,
            data: [
                ["Centro 1", "Grado 1", "Asignatura 1", 1, 1, 1, 1, 1, 1, 1, null],
                ["Centro 2", "Grado 2", "Asignatura 1", 1, 1, 1, 1, 1, 1, 1, null],
                ["Centro 3", "Grado 3", "Asignatura 1", 2, 1, 1, 1, 1, 1, 1, null],
                ["Centro 4", "Grado 4", "Asignatura 1", 1, 1, 1, 1, 1, 1, 1, null]
            ]
        }).render(document.getElementById("tablaGrupos"));
    }

    if (document.getElementById('tablaHoras') != null) {
        new gridjs.Grid({
            columns: [
                "Centro", "Titulación", "Asignatura", "Semestre", "Id Grupo", "Plaza/Docente", "Horas", "Horas totales docente", "Plaza/Docente", "Horas", "Horas totales docente", "Plaza/Docente", "Horas", "Horas totales docente",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<button type="button" class="btn btn-primary" onclick="alert( '${row.cells[0].data}');">Editar</button>`)
                },
            ],
            language: gridjs.l10n.esES,
            sort: true,
            search: true,
            data: [
                ["Centro 1", "Grado 1", "Asignatura 1", 1, 1, "Plaza 1", 1, 1, "Plaza 2", 1, 1, "Plaza 3", 1, 1, null],
                ["Centro 2", "Grado 2", "Asignatura 1", 1, 1, "Docente 1", 1, 1, "Plaza 2", 1, 1, "Plaza 3", 1, 1, null],
                ["Centro 3", "Grado 3", "Asignatura 1", 2, 1, "Plaza 5", 1, 1, "Plaza 3", 1, 1, "Plaza 4", 1, 1, null],
                ["Centro 4", "Grado 4", "Asignatura 1", 1, 1, "Plaza 3", 1, 1, "Plaza 2", 1, 1, "Plaza 3", 1, 1, null]
            ]
        }).render(document.getElementById("tablaHoras"));
    }


});
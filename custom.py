import os

def generation_setup(gen):
	gen.set_copyright_info("<p>© Copyright 2026-present Gabriel Soares.</p>")
	gen.set_favicon_path("$BASE_URL/favicon.svg")

def configure_html_templates(gen):
	gen.add_html_template_from_path(
		'project_sidebar_header', 
		gen.dst_path('templates/sidebar_header.template')
	)

def configure_pages(gen):
	gen.add_documentation_page({
		"name": "Godot RmlUi",
		"location": "/",
		"content": gen.markup_bbcode(gen.get_file_str(gen.dst_path('pages/main.bbcode')))
	})

	gen.add_documentation_page({
		"name": "Getting Started",
		"location": "/getting_started.html",
		"content": gen.markup_bbcode(gen.get_file_str(gen.dst_path('pages/getting_started.bbcode')))
	})

	gen.add_documentation_page({
		"name": "Building",
		"location": "/building.html",
		"content": gen.markup_bbcode(gen.get_file_str(gen.dst_path('pages/building.bbcode')))
	})

def configure_sidebar(gen):
	gen.add_sidebar_item({
		"name": "TUTORIAL",
		"items": [{
			"location": "/getting_started.html",
			"name": "Getting Started"
		}, {
			"location": "/building.html",
			"name": "Building"
		}]
	})

def generation_finished(gen):
	gen.copy_folder(
		gen.dst_path('images'),
		gen.dist_path('resources/images')
	)
	gen.copy_file(
		gen.dst_path('favicon.svg'),
		gen.dist_path('favicon.svg')
	)
	gen.copy_file(
		gen.dst_path('logo.svg'),
		gen.dist_path('logo.svg')
	)


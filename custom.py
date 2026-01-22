import os

def generation_setup(gen):
	gen.set_copyright_info("<p>© Copyright 2026-present Gabriel Soares.</p>")

def configure_pages(gen):
	gen.add_documentation_page({
		"name": "Godot RmlUi",
		"href": "$BASE_URL/",
		"location": "/",
		"filename": gen.dist_path("index.html"),
		"content": gen.markup_bbcode(gen.get_file_str(gen.dst_path('pages/main.bbcode')))
	})

	gen.add_documentation_page({
		"name": "Getting Started",
		"href": "$BASE_URL/tutorial/getting_started.html",
		"location": "/",
		"filename": gen.dist_path("tutorial/getting_started.html"),
		"content": gen.markup_bbcode(gen.get_file_str(gen.dst_path('pages/getting_started.bbcode')))
	})

	gen.add_documentation_page({
		"name": "Building",
		"href": "$BASE_URL/tutorial/building.html",
		"location": "/",
		"filename": gen.dist_path("tutorial/building.html"),
		"content": gen.markup_bbcode(gen.get_file_str(gen.dst_path('pages/building.bbcode')))
	})

def configure_sidebar(gen):
	gen.add_sidebar_item({
		"name": "TUTORIAL",
		"items": [{
			"href": "$BASE_URL/tutorial/getting_started.html",
			"name": "Getting Started"
		}, {
			"href": "$BASE_URL/tutorial/building.html",
			"name": "Building"
		}]
	})

def generation_finished(gen):
	gen.copy_folder(
		gen.dst_path('images'),
		gen.dist_path('resources/images')
	)


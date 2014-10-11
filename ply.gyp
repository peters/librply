# gyp --depth=. -Dtarget_arch=x64 --generator-output=build -G msvs_version=2013

{
  'targets': [
	{
		'target_name': 'librply',
		'type': 'shared_library',
		'include_dirs': [
			'src'
		],
		'defines': [
			'SHARED_LIBRARY'
		],
		'sources': [
			'src/rply.c'
		],
		'direct_dependent_settings': {
			'include_dirs': [
				'src'
			]
		}
	},
	{
		'target_name': 'convert',
		'type': 'executable',
		'dependencies': [
			'librply'
		],
		'sources': [
			'tools/convert.c'
		]
    }
  ]
}
module.exports = {
  purge: [],
  darkMode: 'class', // 'false'or 'media' or 'class'
  theme: {
    extend: {
           spacing: {
			   128: '32rem',
				   },
	},
  },
  variants: {
    extend: {
	    backgroundColor: ['hover', 'responsive', 'dark', 'group-hover', 'focus-within', 'focus'],
	},
  },
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
  ],
  purge: {
    enabled: false,
    content: ['../main/templates/*.html'],
  },
}

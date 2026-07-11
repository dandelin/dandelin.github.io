# frozen_string_literal: true

# Resolve the version placeholders used by third_party_libraries in _config.yml.
# The site keeps third_party_libraries.download disabled, so it does not need the
# remote CSS and asset download machinery from jekyll-3rd-party-libraries.
Jekyll::Hooks.register :site, :after_init do |site|
  libraries = site.config.fetch('third_party_libraries', {})

  libraries.each do |name, library|
    next if name == 'download' || !library.is_a?(Hash)

    version = library['version']
    next if version.to_s.empty?

    replace_version = lambda do |value|
      case value
      when Hash
        value.transform_values { |nested_value| replace_version.call(nested_value) }
      when String
        value.gsub('{{version}}', version)
      else
        value
      end
    end

    library['url'] = replace_version.call(library.fetch('url', {}))
  end
end

class CompleteFish(object):

  def __init__(self, name, output):
    self.name = str(name)
    self.output = output

  def write(self, cmdo, data):
    self.output.write("""
    function __fish_openstack_using_command
        set -l cmd  (commandline -opc)

        if test (count $argv) = 0
            if test (count $cmd) = 1
                return 0
            end
            return 1
        end

        if string match -r "^openstack "(string join " " -- $argv)"\$" (string join " " $cmd)
            return 0
        end

        return 1
    end""" + "\n")

    self.output.write("complete -c openstack -n '__fish_openstack_using_command' -f -a '{0}'\n".format(cmdo))

    for datum in data:
      cmd = datum[0].replace("_", " ")
      args = datum[1]

      self.output.write("complete -c openstack -n '__fish_openstack_using_command {0}' -f -a '{1}'\n".format(cmd,args))
